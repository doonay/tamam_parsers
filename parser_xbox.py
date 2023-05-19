import requests
import json
from datetime import datetime
from insert_in_tables import db_insert

def xbox_parser():
  SESSION = requests.session()
  '''
  headers = {
    'authority': 'catalog.gamepass.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Tue, 28 Mar 2023 04:17:37 GMT',
    'if-none-match': '"0x8DB2F435CFBE303"',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
  }
  '''
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
    title = card['LocalizedProperties'][0]['ProductTitle']
    img = 'https:' + card['LocalizedProperties'][0]['Images'][4]['Uri'] + '?h=60&format=jpg'
    xbox_id = card['ProductId']
    platforms = ['XBOX']
    base_price = float(card["DisplaySkuAvailabilities"][0]["Availabilities"][0]["OrderManagementData"]["Price"]["ListPrice"])
    try:
      discounted_price = float(card["DisplaySkuAvailabilities"][0]["Availabilities"][0]["OrderManagementData"]["Price"]["WholesalePrice"])
      discount = int((base_price - discounted_price) / (base_price / 100))
    except:
      discounted_price = 0
      discount = 0
    last_modified = datetime.now()

    db_insert(
      'xbox',
      xbox_id,
      title,
      platforms,
      base_price,
      discounted_price,
      discount,
      img,
      last_modified
    )
            
    print(f'[INFO] [{game_count}/{last_game}] "{title}" was successfully inserted')
    game_count += 1

if __name__ == '__main__':
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
    db_insert(
      'xbox',
      '29N3TF03KNTBD',
      '2Щенячий патруль: Мега-щенки спасают Бухту Приключений',
      ['2XBOX'],
      229.99,
      220.99,
      22,
      'https://store-images.s-microsoft.com/image/apps.37021.13996206863599819.e2c5aea7-cee9-4965-bcf2-983a449c260d.6960015e-8b1f-4162-800c-9b2c22cc5416?h=60&format=jpg',
      '2023-05-19 10:11:32.664825'
    )