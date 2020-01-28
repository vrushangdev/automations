from __future__ import absolute_import, unicode_literals
import random
import time
from celery.decorators import task
import requests
import json
from .models import ORMMarketSnapShot,ORMMarketChange
import humanize
import datetime
import tweepy
from django.db import models
from .repositories import MarketSnapShotRepo,MarketChangeRepo
from .entities import MarketSnapShot,MarketChange

@task(name="data_to_twitter")
def post_crypto_market_report_to_twitter():
    """
    sets up twitter client , calculate current crypto market report and post it to twitter .
    :return: String status
    """
    api = setUpTwitter()
    prev_shot = ORMMarketSnapShot.objects.all().first()
    snapshot = getMarketSnapShot()
    
    change = MarketChange(
        prev_shot,
        snapshot
    )   
    calculated_change = ORMMarketChange.objects.create(
                        changeInTotalMarketCapPer=change.changeInTotalMarketCapPer,
                        changeInTotalMarketCapUSD=change.changeInTotalMarketCapUSD
                           )

    prepared_text = format_twitter_text(snapshot, calculated_change) 

    status = api.update_status(prepared_text)

   


    return prepared_text



def setUpTwitter():
    ACCESS_TOKEN = "928953443921813505-oe1G9B7ke7aiBMmL7neHt9rlhbVsrtU" 
    ACCESS_TOKEN_SECRET = "eKIMXmsLwa14DTB8HV6mxmIqQlqcw6lr8gsogEk47sD1c"
    API_KEY = "FocdrH9u7fz7Jk1QJAP5UR8Ln"
    API_SECRET="EPwsA8gMlzzfUIoHtjGwqkG3BdOqsu4u5coe55pHDWmsneE0K8"
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET) 
    auth.set_access_token("928953443921813505-oe1G9B7ke7aiBMmL7neHt9rlhbVsrtU", "eKIMXmsLwa14DTB8HV6mxmIqQlqcw6lr8gsogEk47sD1c")
    api = tweepy.API(auth)
    return api


def getMarketSnapShot():
    """
    Fetch market data from 
    coingecko api & create MarketSnapShot Entity ,
    Returns ORMSnapShot Object From Models.py
    """
    res = requests.get("https://api.coingecko.com/api/v3/global")
    data = json.loads(res.text)
    mCapUSD = data['data']['total_market_cap']['usd']
    bitcoinDominancePer = data['data']['market_cap_percentage']['btc']
    repo = MarketSnapShotRepo()
    print("Above Last_Object")
    snapShot =  MarketSnapShot(
       mCapUSD,
       bitcoinDominancePer,
       
    )
    print(snapShot)
    db_snapshot = repo.create_marketsnapshot(snapShot)
    return db_snapshot



def format_twitter_text(snapshot,change):
    """
    Format Data To Be Posted On Twitter From ORMMarketSnapShot Model .
    :param snapshot: CryptoMarketSnapshot
    :type snapshot: ORMMarketSnapShot
    :return: String
    """
    PostText="""
                
                Crypto Market Report \n 
                {} | {:f} % | {} \n 
                Bitcoin Cap Usd : {} \n
                Alts Cap Usd : {} \n
                #crypto #bitcoin #cryptocurrency 
                """.format(
                    humanize.intword(
                        snapshot.totalMarketCapUSD
                    ),
                    change.changeInTotalMarketCapPer,
                    humanize.intword(
                        change.changeInTotalMarketCapUSD
                        ),

                    humanize.intword(
                        snapshot.totalBitcoinMarketCapUSD
                    ),
                    humanize.intword(
                        snapshot.totalAltsMarketCapUSD
                    )

                )
    return PostText
