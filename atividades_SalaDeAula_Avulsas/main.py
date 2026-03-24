

from insert import cadastrar_aluno;
from select import listar_alunos;
from update import atualizar_aluno;
from delete import deletar_aluno;


def menu():

    while True:

        print("""
=================================
        SISTEMA ESCOLA
=================================

1 - Cadastrar aluno
2 - Listar alunos
3 - Atualizar aluno
4 - Excluir aluno
5 - Sair
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            atualizar_aluno()

        elif opcao == "4":
            deletar_aluno()

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()