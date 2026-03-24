from conexao import conectar_banco

def cadastrar_aluno(nome=None, data=None, cpf=None):
    
    conn = conectar_banco()
    
    if conn:
        cursor = conn.cursor()

        # Se a função for chamada sem dados (pelo terminal), ela faz as perguntas
        if nome is None:
            print("\n--- Cadastro de Aluno (via Terminal) ---")
            nome = input("Nome: ")
            data = input("Data de nascimento: ")
            cpf = input("CPF: ")
            

        # O SQL continua o mesmo, garantindo a segurança com %s
        sql = """
        INSERT INTO alunos (nome, data_nascimento, cpf)
        VALUES (%s, %s, %s)
        """

        try:
            cursor.execute(sql, (nome, data, cpf))
            
            conn.commit()
            print(f"DEBUG: Linhas afetadas: {cursor.rowcount}") # Se aparecer 1, o dado FOI enviado!
            print(f"\n[BANCO] Aluno {nome} cadastrado com sucesso!")
            return True # Retorna True para a interface saber que deu certo
        except Exception as e:
            print(f"\n[ERRO] Falha ao inserir no banco: {e}")
            return False # Retorna False se o CPF já existir, por exemplo
        finally:
            cursor.close()
            conn.close()