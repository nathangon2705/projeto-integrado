from flask import Flask, request, jsonify
from flask_cors import CORS

# Inicializa a aplicação Flask
app = Flask(__name__)
# Habilita o CORS para permitir que o frontend (rodando em um arquivo) acesse o backend
CORS(app)

# --- BANCO DE DADOS EM MEMÓRIA ---
# (Em uma aplicação real, isso seria um banco de dados como SQLite, PostgreSQL, etc.)
db = {
    "pacientes": [
        { "id": 1, "nome": 'João da Silva', "idade": 34, "telefone": '11987654321', "debito": 0 },
        { "id": 2, "nome": 'Maria Oliveira', "idade": 45, "telefone": '21912345678', "debito": 150.00 },
    ],
    "medicos": [
        { "id": 1, "nome": 'Dr. Ana Costa', "crm": '12345-SP', "especialidade": 'Cardiologia' },
        { "id": 2, "nome": 'Dr. Bruno Martins', "crm": '67890-RJ', "especialidade": 'Ortopedia' }
    ],
    "tipos_atendimento": [
      { "id": 1, "nome": 'Consulta', "valor": 250.00 },
      { "id": 2, "nome": 'Retorno', "valor": 0.00 },
    ],
    "agenda": [
        { "id": 1, "pacienteId": 1, "medicoId": 1, "tipoAtendimentoId": 1, "data": '2025-09-20', "hora": '10:00', "status": 'agendado' },
    ],
    "pagamentos": []
}

# --- Funções Auxiliares ---
def get_next_id(table):
    """Calcula o próximo ID para uma tabela do 'banco'."""
    if not db[table]:
        return 1
    return max(item['id'] for item in db[table]) + 1

# --- ROTAS DA API ---

# Rota principal para servir o frontend (opcional, mas útil)
@app.route('/')
def index():
    # Idealmente, serviria o index.html aqui
    return "Servidor da Clínica Vida+ está no ar. Acesse os endpoints da API."

# --- Pacientes ---
@app.route('/api/pacientes', methods=['GET'])
def get_pacientes():
    return jsonify(db["pacientes"])

@app.route('/api/pacientes/<int:paciente_id>', methods=['GET'])
def get_paciente(paciente_id):
    paciente = next((p for p in db["pacientes"] if p["id"] == paciente_id), None)
    if paciente:
        return jsonify(paciente)
    return jsonify({"erro": "Paciente não encontrado"}), 404

@app.route('/api/pacientes', methods=['POST'])
def add_paciente():
    data = request.json
    if not data or 'nome' not in data or 'idade' not in data:
        return jsonify({"erro": "Dados incompletos"}), 400
    
    novo_paciente = {
        "id": get_next_id("pacientes"),
        "nome": data["nome"],
        "idade": data["idade"],
        "telefone": data.get("telefone", ""),
        "debito": 0
    }
    db["pacientes"].append(novo_paciente)
    return jsonify(novo_paciente), 201

# --- Médicos ---
@app.route('/api/medicos', methods=['GET'])
def get_medicos():
    return jsonify(db["medicos"])

@app.route('/api/medicos', methods=['POST'])
def add_medico():
    data = request.json
    if not data or 'nome' not in data or 'crm' not in data or 'especialidade' not in data:
        return jsonify({"erro": "Dados incompletos"}), 400
        
    novo_medico = {
        "id": get_next_id("medicos"),
        "nome": data["nome"],
        "crm": data["crm"],
        "especialidade": data["especialidade"]
    }
    db["medicos"].append(novo_medico)
    return jsonify(novo_medico), 201

# --- Tipos de Atendimento ---
@app.route('/api/tipos_atendimento', methods=['GET'])
def get_tipos_atendimento():
    return jsonify(db["tipos_atendimento"])

@app.route('/api/tipos_atendimento', methods=['POST'])
def add_tipo_atendimento():
    data = request.json
    if not data or 'nome' not in data or 'valor' not in data:
        return jsonify({"erro": "Dados incompletos"}), 400
    
    novo_tipo = {
        "id": get_next_id("tipos_atendimento"),
        "nome": data["nome"],
        "valor": float(data["valor"])
    }
    db["tipos_atendimento"].append(novo_tipo)
    return jsonify(novo_tipo), 201

# --- Agenda ---
@app.route('/api/agenda', methods=['GET'])
def get_agenda():
    # Enriquecer os dados da agenda com nomes para facilitar no frontend
    agenda_enriquecida = []
    for agendamento in db["agenda"]:
        paciente = next((p for p in db["pacientes"] if p["id"] == agendamento["pacienteId"]), None)
        medico = next((m for m in db["medicos"] if m["id"] == agendamento["medicoId"]), None)
        tipo = next((t for t in db["tipos_atendimento"] if t["id"] == agendamento["tipoAtendimentoId"]), None)
        
        if paciente and medico and tipo:
            agenda_enriquecida.append({
                **agendamento,
                "nomePaciente": paciente["nome"],
                "nomeMedico": medico["nome"],
                "nomeAtendimento": tipo["nome"]
            })
    return jsonify(agenda_enriquecida)

@app.route('/api/agenda', methods=['POST'])
def add_agendamento():
    data = request.json
    paciente_id = data.get("pacienteId")
    tipo_atendimento_id = data.get("tipoAtendimentoId")

    # 1. Validações
    paciente = next((p for p in db["pacientes"] if p["id"] == paciente_id), None)
    if not paciente:
        return jsonify({"erro": "Paciente não encontrado"}), 404
    
    tipo_atendimento = next((t for t in db["tipos_atendimento"] if t["id"] == tipo_atendimento_id), None)
    if not tipo_atendimento:
        return jsonify({"erro": "Tipo de atendimento não encontrado"}), 404

    # 2. Trava de agendamento por débito
    if paciente["debito"] > 0:
        return jsonify({"erro": f"Agendamento bloqueado. Paciente {paciente['nome']} possui um débito de R${paciente['debito']:.2f}."}), 403 # Forbidden

    if not all(k in data for k in ["medicoId", "data", "hora"]):
        return jsonify({"erro": "Dados incompletos para o agendamento"}), 400

    # 3. Adicionar agendamento e débito
    novo_agendamento = {
        "id": get_next_id("agenda"),
        "pacienteId": paciente_id,
        "medicoId": data["medicoId"],
        "tipoAtendimentoId": tipo_atendimento_id,
        "data": data["data"],
        "hora": data["hora"],
        "status": "agendado"
    }
    db["agenda"].append(novo_agendamento)
    
    # Adiciona o valor do atendimento ao débito do paciente
    paciente["debito"] += tipo_atendimento["valor"]
    
    return jsonify(novo_agendamento), 201

# --- Pagamentos ---
@app.route('/api/pagamentos', methods=['POST'])
def add_pagamento():
    data = request.json
    if not data or 'pacienteId' not in data or 'valor' not in data:
        return jsonify({"erro": "Dados incompletos"}), 400
        
    paciente_id = data["pacienteId"]
    valor_pago = float(data["valor"])

    paciente = next((p for p in db["pacientes"] if p["id"] == paciente_id), None)
    if not paciente:
        return jsonify({"erro": "Paciente não encontrado"}), 404

    paciente["debito"] -= valor_pago
    if paciente["debito"] < 0:
        paciente["debito"] = 0 # Evita débito negativo

    novo_pagamento = {
        "id": get_next_id("pagamentos"),
        "pacienteId": paciente_id,
        "valor": valor_pago,
        "data": "hoje" # Simplificado, poderia usar datetime
    }
    db["pagamentos"].append(novo_pagamento)
    
    return jsonify({"sucesso": "Pagamento registrado.", "paciente": paciente})

# --- Histórico ---
@app.route('/api/historico/<int:paciente_id>', methods=['GET'])
def get_historico_paciente(paciente_id):
    historico = [atendimento for atendimento in db["agenda"] if atendimento["pacienteId"] == paciente_id]
    return jsonify(historico)

# --- Relatórios ---
@app.route('/api/relatorios/atendimentos_por_paciente', methods=['GET'])
def relatorio_atendimentos():
    relatorio = []
    for paciente in db["pacientes"]:
        count = sum(1 for atendimento in db["agenda"] if atendimento["pacienteId"] == paciente["id"])
        relatorio.append({
            "pacienteId": paciente["id"],
            "nomePaciente": paciente["nome"],
            "totalAtendimentos": count
        })
    return jsonify(relatorio)

# --- Healthcheck ---
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

# --- Ponto de partida para rodar o servidor ---
if __name__ == '__main__':
    # O host='0.0.0.0' torna o servidor acessível na sua rede local
    # A porta 5000 é a padrão do Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
