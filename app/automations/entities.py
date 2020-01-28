class MarketSnapShot:
    def __init__(self,totalMarketCapUSD,bitcoinDominancePercentage,id=None):
        self.totalMarketCapUSD = totalMarketCapUSD
        self.bitcoinDominancePercentage = bitcoinDominancePercentage


    @property
    def altsMarketDominancePercentage(self):
        """
        Calculates Percentage of altcoin market share .
        """
        return float(100 - self.bitcoinDominancePercentage)
    
    @property
    def bitcoinMarketCapUSD(self):
        """
        Calculates Total market cap of bitcoin in usd .
        """
        return float((self.bitcoinDominancePercentage * self.totalMarketCapUSD) / 100)
    
    @property
    def altsMarketCapUSD(self):
        """
        Calculates Totall market cap of all the alt coins in usd .
        """
        return float( (self.altsMarketDominancePercentage * self.totalMarketCapUSD) / 100)



class MarketChange:
    def __init__(self,old,new):
        self.old=old
        self.new =new
    @property
    def changeInTotalMarketCapUSD(self):
        """
        Calculates total change in market cap of crypto market : Return differnce between new & old objects .  .
        """
        return float(
            (float(self.new.totalMarketCapUSD) - float(self.old.totalMarketCapUSD) )
            )

    @property
    def changeInTotalMarketCapPer(self):
        """
        Calculates total percentage change in market cap of crypto market : Return differnce between new & old objects .  .
        """
        return float(((float(self.changeInTotalMarketCapUSD)/float(self.old.totalMarketCapUSD)) / 100))
    