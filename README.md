# Sistema de Gerenciamento para Clínica Vida+

Este é um sistema web simples e moderno para gerenciar os processos diários de uma pequena clínica, incluindo o controle de pacientes, médicos, agendamentos e finanças.

O projeto foi desenvolvido com uma arquitetura cliente-servidor, utilizando Python e Flask no backend para toda a lógica de negócio e HTML/CSS/JavaScript puro no frontend para a interface do usuário.

## ✨ Funcionalidades Principais

*   **Cadastro Geral:** Módulos para registrar Pacientes, Médicos e os Tipos de Atendimento oferecidos, com seus respectivos valores.
*   **Agenda Inteligente:**
    *   Criação de agendamentos vinculando paciente, médico e tipo de atendimento.
    *   Ao agendar, o valor do atendimento é automaticamente lançado no débito do paciente.
*   **Controle Financeiro:**
    *   **Bloqueio por Débito:** O sistema impede novos agendamentos para pacientes com pendências financeiras.
    *   **Registro de Pagamentos:** Uma tela dedicada para registrar pagamentos e abater os débitos dos pacientes.
    *   **Visualização de Débitos:** A lista de pacientes exibe claramente o saldo devedor de cada um.
*   **Histórico e Relatórios:**
    *   **Histórico do Paciente:** Visualize todos os atendimentos de um paciente específico.
    *   **Relatório Simples:** Gere um relatório que mostra o número total de atendimentos por paciente.
*   **Interface Moderna:**
    *   Layout limpo e organizado com menu lateral.
    *   Tema claro e escuro para melhor conforto visual.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o sistema na sua máquina.

### 1. Pré-requisitos

*   É necessário ter o **Python 3** instalado no seu computador. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

### 2. Instalação das Dependências

Abra um terminal (como o PowerShell ou CMD) na pasta do projeto e execute o seguinte comando para instalar as bibliotecas que o backend precisa:

```bash
pip install Flask Flask-Cors
```

### 3. Iniciando o Servidor (Backend)

Ainda no terminal, na pasta do projeto, execute o script principal do Python:

```bash
python app.py
```

Você verá algumas mensagens indicando que o servidor está rodando em `http://127.0.0.1:5000/`. **Deixe este terminal aberto**; ele é o cérebro do sistema.

### 4. Abrindo a Interface (Frontend)

Agora, basta abrir o arquivo `index.html` no seu navegador de preferência (Google Chrome, Firefox, etc.). Você pode fazer isso clicando duas vezes no arquivo.

Pronto! O sistema estará funcionando, com a interface se comunicando com o seu servidor local.

## 🛠️ Tecnologias Utilizadas

*   **Backend:** Python 3, Flask
*   **Frontend:** HTML5, CSS3, JavaScript (puro, sem frameworks)
*   **Comunicação:** API REST
