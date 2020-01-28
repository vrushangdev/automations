from django.db import models
from datetime import datetime
# Create your models here.
class ORMMarketChange(models.Model):
        changeInTotalMarketCapPer = models.DecimalField(decimal_places=8,max_digits=28)
        changeInTotalMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=30)


class ORMMarketSnapShot(models.Model):
        totalMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=28)
        totalBitcoinMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=28)
        totalAltsMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=28)
        bitcoinDominancePer = models.DecimalField(decimal_places=8,max_digits=28)
        altsDominancePer = models.DecimalField(decimal_places=8,max_digits=28)
        created_at = models.DateTimeField(auto_now=True)


