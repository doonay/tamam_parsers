import sys
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models_alchemy import Game
from config import db_name, user, password, host, port

def main(company):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
    metadata = MetaData()
    metadata.reflect(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Deleting the table
        table_name = Game.table_name(company)
        table = metadata.tables[table_name]
        table.drop(bind=engine)
        session.commit()

        print("[INFO] Table deleted successfully")

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
        print("\tpython table_delete_alchemy.py xbox")
        print("\tpython table_delete_alchemy.py playstation")
