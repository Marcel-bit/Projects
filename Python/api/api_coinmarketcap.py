from requests import Request, Session
import json
import pprint
import time

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
parameters = {
  'slug':'bitcoin',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b85f5036-a692-47a4-8090-540829ba1b64',
}

session = Session()
session.headers.update(headers)

for x in range(5):
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data['data']['1']['quote']['USD']['price'])
    except:
      print("Error")
    time.sleep(3)