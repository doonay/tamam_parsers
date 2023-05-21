import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, JSON, SmallInteger, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from models_alchemy import Game
from config import db_name, user, password, host, port

def create_table(company):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
    metadata = MetaData()

    # Определение структуры таблицы
    table_name = Game.table_name(company)
    table = Table(
        table_name,
        metadata,
        Column('id', Integer, primary_key=True),
        Column('game_id', String),
        Column('title', String),
        Column('platforms', JSON),
        Column('base_price', Integer),
        Column('discounted_price', Integer),
        Column('discount', SmallInteger),
        Column('img', String),
        Column('last_modified', TIMESTAMP),
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Создание таблицы
        metadata.create_all(bind=engine)

        print("[INFO] Table created successfully")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL:", ex)
    finally:
        session.close()
        print("[INFO] PostgreSQL connection closed")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        create_table(sys.argv[1])
    else:
        print("Company name not specified. Please provide a company name when executing the script.")
        print("For example:")
        print("\tpython table_create_alchemy.py xbox")
        print("\tpython table_create_alchemy.py playstation")
