import psycopg2
import json
import time

def read_data(conn_params):
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()

        start_time = time.time()

        cursor.execute("SELECT dados FROM pessoas")
        records = cursor.fetchall()

        for record in records:
            data = json.loads(record[0])
            print(json.dumps(data, indent=2, ensure_ascii=False))

        end_time = time.time()
        execution_time = end_time - start_time

        print('Todos os dados foram lidos com sucesso.')
        print(f'Tempo de execução: {execution_time:.2f} segundos.')

    except psycopg2.Error as e:
        print(f"Erro ao ler dados: {e}")

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

read_data(conn_params)
