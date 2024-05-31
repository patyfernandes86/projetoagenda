alunos = {}

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    alunos[matricula] = nome
    print("Aluno adicionado com sucesso!")

def remover_aluno():
    matricula = input("Digite o número de matrícula do aluno que deseja remover: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def visualizar_alunos():
    if alunos:
        print("Lista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Número de matrícula: {matricula}, Nome: {nome}")
    else:
        print("Não há alunos registrados.")

while True:
    print("\nOpções:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        remover_aluno()
    elif opcao == "3":
        visualizar_alunos()
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")