




def conectar_banco():
    try:
        # Configurações de conexão (ajuste conforme seu banco)
        conexao = mysql.connector.connect(
            host='localhost',
            database='escola', # O banco deve existir ou ser criado
            user='root',       # Usuário padrão
            password=''        # Sua senha do MySQL
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            data_nascimento VARCHAR(10),
            cpf VARCHAR(14) UNIQUE
        )
    """)
    conexao.commit()

def cadastrar_aluno():
    conn = conectar_banco()
    if conn and conn.is_connected():
        criar_tabela(conn)
        cursor = conn.cursor()

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

