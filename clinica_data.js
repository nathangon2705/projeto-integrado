// Dados simulados para médicos, pacientes, atendimentos, pagamentos, tipos de atendimento
let pacientes = [
    { id: 1, nome: 'João da Silva', idade: 34, telefone: '11987654321', debito: 0 },
    { id: 2, nome: 'Maria Oliveira', idade: 45, telefone: '21912345678', debito: 150.00 },
    { id: 3, nome: 'Carlos Pereira', idade: 29, telefone: '31999998888', debito: 0 }
];
let medicos = [
    { id: 1, nome: 'Dr. Ana Costa', crm: '12345-SP', especialidade: 'Cardiologia' },
    { id: 2, nome: 'Dr. Bruno Martins', crm: '67890-RJ', especialidade: 'Ortopedia' }
];
let tiposAtendimento = [
  { id: 1, nome: 'Consulta', valor: 250.00 },
  { id: 2, nome: 'Retorno', valor: 0.00 },
  { id: 3, nome: 'Exame de Sangue', valor: 120.00 }
];
let agenda = [
    { id: 1, pacienteId: 1, medicoId: 1, tipoAtendimentoId: 1, data: '2025-09-20', hora: '10:00', status: 'agendado' },
    { id: 2, pacienteId: 3, medicoId: 2, tipoAtendimentoId: 2, data: '2025-09-20', hora: '14:30', status: 'agendado' }
];
let pagamentos = [];
