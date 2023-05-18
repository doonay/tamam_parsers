#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import psycopg2
from config import host, user, password, db_name

def main(tablename):
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
            
        
        # delete a table
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                DROP TABLE {tablename};
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
        print("Table name not specified. Please provide a table name when executing the script.")
        print("For example: python delete_table.py tablename")