from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY
}

session = Session()
session.headers.update(headers)

list1 = []
count = 0

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  for listing in data:
    if count <= 5:
        print(data['data'][0]['symbol'])
        list.append(data['data'][0]['symbol'])
        count += 1
  print(list(list1))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)