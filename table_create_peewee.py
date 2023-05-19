import sys
from peewee import *
from models import Game

def main(company):
    try:
        # Создание таблицы
        with Game._meta.database.connection():
            table_name = f'{company}_games'
            Game._meta.table_name = table_name  # Установка имени таблицы для модели
            Game.create_table()
        
        print("[INFO] Table created successfully")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL:", ex)
    finally:
        Game._meta.database.close()
        print("[INFO] PostgreSQL connection closed")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Company name not specified. Please provide a company name when executing the script.")
        print("For example:")
        print("\tpython create_table.py xbox")
        print("\tpython create_table.py playstation")