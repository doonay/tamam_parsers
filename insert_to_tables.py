'''
Модуль заполняет таблицы на основании переданных в него данных из парсеров соответственно.
Если это xbox, то данные вносятся в таблицу xbox, если playstation - в playstation.
Парсеры площадок будут добавляться постепенно разные, но возвращаемые из парсеров данные должны быть унифицированы:
<company>: str
<company>_id: str
title: str
platforms: list
base_price: float (10 знаков, 2 из них после запятой)
discounted_price: float (10 знаков, 2 из них после запятой)
discount: int
img: str
'''
import psycopg2
from config import host, user, password, db_name
import json
from datetime import datetime

def db_insert(
        company_name,
        game_id,
        title,
        platforms,
        base_price,
        discounted_price,
        discount,
        img,
        last_modified=datetime.now()
        ):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
        )
        
        connection.autocommit = True 

        # insert data into a table
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                INSERT INTO {company_name}_games (
                    game_id,
                    title,
                    platforms,
                    base_price,
                    discounted_price,
                    discount,
                    img,
                    last_modified
                ) VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s);
                """,
                (game_id, title, platforms, base_price, discounted_price, discount, img, last_modified)
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    db_insert(
        'xbox',
        '9N3TF03KNTBD',
        'Щенячий патруль: Мега-щенки спасают Бухту Приключений',
        json.dumps(['XBOX', 'PS4']),
        29.99,
        20.99,
        30,
        'https://store-images.s-microsoft.com/image/apps.37021.13996206863599819.e2c5aea7-cee9-4965-bcf2-983a449c260d.6960015e-8b1f-4162-800c-9b2c22cc5416?h=60&format=jpg',
    )
    '''
    db_insert(
        'playstation',
        'EP7072-CUSA37356_00-ZOOLREDIMENSIOND',
        'Zool Redimensioned',
        ['PS4'],
        7900,
        7900,
        0,
        'https://image.api.playstation.com/vulcan/ap/rnd/202303/2920/6a8994670918ac434bf1ca56e932264892847fce7c38e73b.png',
        '2023-05-18 12:18:31.915173'
    )
    '''