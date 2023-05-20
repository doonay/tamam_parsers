import sys
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from models_alchemy import Game
from config import db_name, user, password, host, port

def main(company):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
    metadata = MetaData()

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Создание таблицы
        table_name = Game.table_name(company)
        table = Table(table_name, metadata)
        table.create(bind=engine)
        session.commit()

        print("[INFO] Table created successfully")

    except Exception as ex:
        session.rollback()
        print("[INFO] Error while working with PostgreSQL:", ex)
    finally:
        session.close()
        print("[INFO] PostgreSQL connection closed")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Company name not specified. Please provide a company name when executing the script.")
        print("For example:")
        print("\tpython table_create_alchemy.py xbox")
        print("\tpython table_create_alchemy.py playstation")
