CREATE TABLE IF NOT EXISTS alunos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            data_nascimento VARCHAR(10),
            cpf VARCHAR(14) UNIQUE
        )

        print("--- Cadastro de Aluno no Banco de Dados ---")
        nome = input("Nome: ").strip()
        data_nasc = input("Data de Nascimento (DD/MM/AAAA): ").strip()
        cpf = input("CPF (apenas números): ").strip()

        # Comando SQL para inserção
        sql = "INSERT INTO alunos (nome, data_nascimento, cpf) VALUES (%s, %s, %s)"
        valores = (nome, data_nasc, cpf)

        try:
            cursor.execute(sql, valores)
            conn.commit() # Salva as alterações
            print(f"\nSucesso! {cursor.rowcount} registro(s) inserido(s).")
        except Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    cadastrar_aluno()

-- se der erro no CMD, ta aqui a solução:
C:\Users\CAS-MT>cd Documents\atividades --comando que seleciona a pasta

C:\Users\CAS-MT\Documents\atividades>py aluno.py
Traceback (most recent call last):
  File "C:\Users\CAS-MT\Documents\atividades\aluno.py", line 1, in <module>
    import mysql.connector
ModuleNotFoundError: No module named 'mysql'
--o erro

C:\Users\CAS-MT\Documents\atividades>python -m pip install mysql-connector-python
Requirement already satisfied: mysql-connector-python in C:\Users\CAS-MT\AppData\Local\Programs\Python\Python313\Lib\site-packages (9.6.0)
--tem q dar essa resposta
C:\Users\CAS-MT\Documents\atividades>python -c "import mysql.connector; print('mysql connector OK')"
mysql connector OK
--tem q dar essa resposta tb
C:\Users\CAS-MT\Documents\atividades>python aluno.py -- agora é só usar e ser feliz