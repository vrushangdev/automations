from django.test import TestCase
from .. import models
class ModelTests(TestCase):
    """
    Includes tests for all models in automations app . 
    """

    def test_market_data_fields_are_double(self):
        """
        -   Total_Market_Capitalization_USD : Double
        -   BTC_Dominance_Percentage : Double
        -   ALTS_Dominance_Percentage : Double
        -   BTC_Mcap_USD : Double
        -   ALTS_Mcap_USD : Double
        """
        
        totalMarketCapUSD = 100
        totalBitcoinMarketCapUSD = 65.36
        totalAltsMarketCapUSD = 34.67
        bitcoinDominancePer = 80
        altsDominancePer = 20
        changeInTotalMarketCapPer = 12
        changeInTotalMarketCapUSD = 120
        changeInBitcoinMarketCapPer = 12
        changeInBitcoinMarketCapUSD = 120
        changeInAltsMarketCapPer = 12
        changeInAltsMarketCapUSD = 120

        # Lets create Model Then test
        marketSnapshot = models.CryptoMarketReport.objects.create(
            totalMarketCapUSD=totalMarketCapUSD,
            totalBitcoinMarketCapUSD=totalBitcoinMarketCapUSD,
            totalAltsMarketCapUSD=totalAltsMarketCapUSD,
            bitcoinDominancePer=bitcoinDominancePer,
            altsDominancePer=altsDominancePer,
            changeInTotalMarketCapPer=changeInTotalMarketCapPer,
            changeInTotalMarketCapUSD=changeInTotalMarketCapUSD,
            changeInBitcoinMarketCapPer=changeInBitcoinMarketCapPer,
            changeInBitcoinMarketCapUSD=changeInBitcoinMarketCapUSD,
            changeInAltsMarketCapPer=changeInAltsMarketCapPer,
            changeInAltsMarketCapUSD=changeInAltsMarketCapUSD)
        
        self.assertEquals(totalMarketCapUSD,marketSnapshot.totalMarketCapUSD)



