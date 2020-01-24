from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
import requests
import json
ACCESS_TOKEN = "928953443921813505-1kZuzqrf5uzlMhcB7ndEhATE9z8srWg"
ACCESS_TOKEN_SECRET = "1O1BtAtXaElYRFvJRaof63MciillAniqJGAM9gnJz0lCS"
API_KEY = "FocdrH9u7fz7Jk1QJAP5UR8Ln"
API_SECRET="EPwsA8gMlzzfUIoHtjGwqkG3BdOqsu4u5coe55pHDWmsneE0K8"


@task(name="data_to_twitter")
def post_crypto_market_report_to_twitter():
    res = requests.get("https://api.coingecko.com/api/v3/global")
    data = json.loads(res.text)
    mCapUSD = data['data']['total_market_cap']['usd']
    print(mCapUSD)
    return mCapUSD

