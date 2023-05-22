import requests
import json
from datetime import datetime
from insert_to_tables import db_insert

def xbox_parser():
  SESSION = requests.session()
  url = 'https://catalog.gamepass.com/sigls/v2?id=f6f1f99f-9b49-4ccd-b3bf-4d9767a77f5e&language=ru-ru&market=RU'
  r = SESSION.get(url)

  all_xbox_games_ids = json.loads(r.text)
  ids_list = []
  for xbox_game in range(1, len(all_xbox_games_ids), 1):
    ids_list.append(all_xbox_games_ids[xbox_game]['id'])
  ids_list = ','.join(ids_list)

  last_game = len(ids_list)

  url = f'https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds={ids_list}&market=RU&languages=RU-RU&MS-CV=DGU1mcuYo0WMMp+F.1'
  r = SESSION.get(url)
  data = json.loads(r.text)['Products']

  game_count = 0
  for card in data:
    company = 'xbox'
    game_id = card['ProductId']
    title = card['LocalizedProperties'][0]['ProductTitle']
    platforms = ['XBOX']
    base_price = float(card["DisplaySkuAvailabilities"][0]["Availabilities"][0]["OrderManagementData"]["Price"]["ListPrice"])
    try:
      discounted_price = float(card["DisplaySkuAvailabilities"][0]["Availabilities"][0]["OrderManagementData"]["Price"]["WholesalePrice"])
      discount = int((base_price - discounted_price) / (base_price / 100))
    except:
      discounted_price = 0
      discount = 0
    img = 'https:' + card['LocalizedProperties'][0]['Images'][4]['Uri'] + '?h=60&format=jpg'

    db_insert(
      company,
      game_id,
      title,
      platforms,
      base_price,
      discounted_price,
      discount,
      img
    )
            
    print(f'[INFO] [{game_count}/{last_game}] "{title}" was successfully inserted')
    game_count += 1

if __name__ == '__main__':
    db_insert(
        'xbox',
        '403TF03KNTBD',
        'Super puper game1',
        json.dumps(['XBOX', 'PS4']),
        19.99,
        10.99,
        10,
        'https://store-images.s-microsoft.com/image/apps.37021.13996206863599819.e2c5aea7-cee9-4965-bcf2-983a449c260d.6960015e-8b1f-4162-800c-9b2c22cc5416?h=60&format=jpg',
    )