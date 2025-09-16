# Sistema de gerenciamento de pacientes para a Clínica Vida+
# Autor: (adicione seu nome se quiser)

pacientes = []  # Lista de dicionários: {"nome": str, "idade": int, "telefone": str}


def cadastrar_paciente(lista_pacientes):
    """Pede nome, idade e telefone. Valida idade como inteiro positivo. Adiciona à lista."""
    print("\n=== Cadastro de Paciente ===")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return
    # Validação da idade
    while True:
        idade_str = input("Idade: ").strip()
        if not idade_str.isdigit():
            print("Idade deve ser um número inteiro positivo.")
            continue
        idade = int(idade_str)
        if idade <= 0:
            print("Idade deve ser maior que zero.")
            continue
        break
    telefone = input("Telefone: ").strip()
    if not telefone:
        telefone = "(não informado)"

    registro = {"nome": nome, "idade": idade, "telefone": telefone}
    lista_pacientes.append(registro)
    print(f"Paciente '{nome}' cadastrado com sucesso! Total agora: {len(lista_pacientes)}")


def calcular_estatisticas(lista_pacientes):
    """Calcula e imprime total, idade média, mais novo e mais velho. Lida com lista vazia."""
    print("\n=== Estatísticas ===")
    if not lista_pacientes:
        print("Nenhum paciente cadastrado.")
        return
    total = len(lista_pacientes)
    idades = [p["idade"] for p in lista_pacientes]
    media = sum(idades) / total
    mais_novo = min(lista_pacientes, key=lambda p: p["idade"])
    mais_velho = max(lista_pacientes, key=lambda p: p["idade"])
    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.1f}")
    print(f"Mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")


def buscar_paciente(lista_pacientes):
    """Busca por nome (parcial, case-insensitive) e mostra resultados."""
    print("\n=== Buscar Paciente ===")
    if not lista_pacientes:
        print("Nenhum paciente cadastrado.")
        return
    termo = input("Digite parte do nome para buscar: ").strip().lower()
    if not termo:
        print("Termo de busca vazio.")
        return
    encontrados = [p for p in lista_pacientes if termo in p["nome"].lower()]
    if not encontrados:
        print("Nenhum paciente encontrado.")
        return
    print(f"Encontrados {len(encontrados)} paciente(s):")
    for idx, p in enumerate(encontrados, 1):
        print(f" {idx}. {p['nome']} - {p['idade']} anos - Tel: {p['telefone']}")


def listar_pacientes(lista_pacientes):
    """Lista todos os pacientes de forma organizada."""
    print("\n=== Lista de Pacientes ===")
    if not lista_pacientes:
        print("Nenhum paciente cadastrado.")
        return
    for i, p in enumerate(lista_pacientes, 1):
        print(f"{i:02d}. {p['nome']} - {p['idade']} anos - Tel: {p['telefone']}")
    print(f"-- Total: {len(lista_pacientes)} paciente(s) --")


def mostrar_menu():
    print("\n===== MENU CLÍNICA VIDA+ =====")
    print("1 - Cadastrar paciente")
    print("2 - Estatísticas")
    print("3 - Buscar paciente")
    print("4 - Listar pacientes")
    print("5 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            cadastrar_paciente(pacientes)
        elif opcao == '2':
            calcular_estatisticas(pacientes)
        elif opcao == '3':
            buscar_paciente(pacientes)
        elif opcao == '4':
            listar_pacientes(pacientes)
        elif opcao == '5':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
