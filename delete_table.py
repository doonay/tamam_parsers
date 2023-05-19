'''
Утилита удаления таблицы из базы
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
        
        # delete a table
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                DROP TABLE {company}_games;
                """
            )

            print("[INFO] Table was deleted")

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
        print("\tpython delete_table.py xbox")
        print("\tpython delete_table.py playstation")