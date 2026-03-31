import psycopg2
from psycopg2 import Error

    
import psycopg2
from psycopg2 import Error

def conectar_banco():
    try:
        # Tente escrever o nome do banco sem aspas extras primeiro
        # Se o erro persistir, o problema pode estar no 'host' ou na 'senha'
        conexao = psycopg2.connect(
            host="127.0.0.1", # Usar o IP local evita erros de decodificação de nome
            database="Teste do Arthur",
            user="postgres",
            password="12345",
            port="5432"
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None
