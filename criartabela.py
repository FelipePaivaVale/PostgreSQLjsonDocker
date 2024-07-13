import psycopg2
from psycopg2 import sql

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="JsonGerador",
    user="postgres",
    password='12345678',
    host="localhost",
    port="5432"
)

# Criar um cursor
cur = conn.cursor()

# Criar o esquema da tabela
create_table_query = """
CREATE TABLE IF NOT EXISTS contatos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    endereco TEXT NOT NULL,
    data_nascimento DATE NOT NULL
);
"""

# Executar o comando de criação da tabela
cur.execute(create_table_query)

# Confirmar a transação
conn.commit()

# Fechar o cursor e a conexão
cur.close()
conn.close()

print("Tabela criada com sucesso!")
