from django.db import models

# Create your models here.

class CryptoMarketReport(models.Model):
        totalMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=28)
        totalBitcoinMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=28)
        totalAltsMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=28)
        bitcoinDominancePer = models.DecimalField(decimal_places=8,max_digits=28)
        altsDominancePer = models.DecimalField(decimal_places=8,max_digits=28)
        changeInTotalMarketCapPer = models.DecimalField(decimal_places=8,max_digits=28)
        changeInTotalMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=28)
        changeInBitcoinMarketCapPer = models.DecimalField(decimal_places=8,max_digits=28)
        changeInBitcoinMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=28)
        changeInAltsMarketCapPer = models.DecimalField(decimal_places=8,max_digits=28)
        changeInAltsMarketCapUSD = models.DecimalField(decimal_places=8,max_digits=28)
        # created_at = models.DateTimeField(auto_now=True)