##função insert
Insert.py 

from conexao import conectar_banco

def cadastrar_aluno():

    conn = conectar_banco()

    if conn:

        cursor = conn.cursor()

        print("\n--- Cadastro de Aluno ---")

        nome = input("Nome: ")
        data = input("Data de nascimento: ")
        cpf = input("CPF: ")

        sql = """
        INSERT INTO alunos (nome, data_nascimento, cpf)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (nome, data, cpf))
        conn.commit()

        print("\nAluno cadastrado com sucesso!")

        cursor.close()
        conn.close()
##Main (ainda n sei)
Main.py

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

##função select
Select.py

from conexao import conectar_banco

def listar_alunos():

    conn = conectar_banco()

    if conn:

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM alunos ORDER BY nome")

        alunos = cursor.fetchall()

        print("\n======================================================")
        print("                     LISTA DE ALUNOS")
        print("======================================================")

        print(f"{'ID':<5}{'NOME':<20}{'DATA NASC':<15}{'CPF':<15}")
        print("------------------------------------------------------")

        for aluno in alunos:

            print(f"{aluno[0]:<5}{aluno[1]:<20}{aluno[2]:<15}{aluno[3]:<15}")

        print("======================================================")

        cursor.close()
        conn.close()

## conexão com o banco de dados

conexao.py

import psycopg2
from psycopg2 import Error

def conectar_banco():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="escola",
            user="postgres",
            password="1234",
            port=5432
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

##função update
updade.py




from conexao import conectar_banco

def atualizar_aluno():

    conn = conectar_banco()

    if conn:

        cursor = conn.cursor()

        id_aluno = input("Digite o ID do aluno: ")
        novo_nome = input("Novo nome: ")

        sql = "UPDATE alunos SET nome = %s WHERE id = %s"

        cursor.execute(sql, (novo_nome, id_aluno))
        conn.commit()

        print("Aluno atualizado com sucesso!")

        cursor.close()
        conn.close()

##função delete

delete.py


from conexao import conectar_banco

def deletar_aluno():

    conn = conectar_banco()

    if conn:

        cursor = conn.cursor()

        id_aluno = input("Digite o ID do aluno que deseja excluir: ")

        sql = "DELETE FROM alunos WHERE id = %s"

        cursor.execute(sql, (id_aluno,))
        conn.commit()

        print("Aluno excluído com sucesso!")

        cursor.close()
        conn.close()
