'''
Утилита создания таблицы в базе
Параметром принимает имя компании
Команда для запуска например:
python delete_table playstation
или
python delete_table xbox
'''
import sys
import psycopg2
from config import host, user, password, db_name

def main(company):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
        )
        
        connection.autocommit = True 

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version()"
            )
            version_row = cursor.fetchone()  # Получение одной записи результата
            server_version = version_row[0]  # Обращение к первому элементу записи (версии)
            print("Server version:", server_version)  # Вывод версии сервера
        
        # create new table
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                CREATE TABLE {company}_games(
                    id serial PRIMARY KEY,
                    {company}_id varchar(250) NOT NULL,
                    title varchar(250) NOT NULL,
                    platforms varchar(10)[],
                    base_price numeric(10, 2) NOT NULL,
                    discounted_price numeric(10, 2),
                    discount integer,
                    img varchar(250) NOT NULL,
                    last_modified timestamp
                );
                """
            )
        
        print("[INFO] Table created successfully")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

if __name__ == '__main__':
    if len (sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Company name not specified. Please provide a company name when executing the script.")
        print("For example:")
        print("\tpython create_table.py xbox")
        print("\tpython create_table.py playstation")