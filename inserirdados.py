import psycopg2
import json
import time

def insert_data(conn_params, json_file):
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        start_time = time.time()

        for record in data:
            json_str = json.dumps(record)
            cursor.execute("INSERT INTO pessoas (dados) VALUES (%s)", (json_str,))

        conn.commit()

        end_time = time.time()
        execution_time = end_time - start_time

        print(f'Todos os dados do arquivo {json_file} foram inseridos com sucesso.')
        print(f'Tempo de execução: {execution_time:.2f} segundos.')

    except psycopg2.Error as e:
        print(f"Erro ao inserir dados: {e}")

    finally:
        if conn is not None:
            cursor.close()
            conn.close()

conn_params = {
    'dbname': 'JsonGerador',
    'user': 'postgres',
    'password': '12345678',
    'host': 'localhost',  
    'port': 5432  
}

json_file = 'dados.json'

insert_data(conn_params, json_file)
