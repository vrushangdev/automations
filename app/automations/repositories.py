from .entities import MarketSnapShot
from .models import ORMMarketSnapShot,ORMMarketChange


class MarketSnapShotRepo:
    """
    This is repository to manage data of MarketSnapShot
    """

    def _decode_db_marketsnapshot(self,db_snapshot):
        """
        Adapter that converts Djangos built in orm objects to entities .
        """

        return MarketSnapShot(
            id = db_snapshot._id,
            totalMarketCapUSD = db_snapshot.totalMarketCapUSD,
            bitcoinDominancePercentage=db_snapshot.bitcoinDominancePer,
            )
    def get_last_object(self):
        """
        get last stored model of type ORMMarketSnapShot From Our Database .
        """
        return (ORMMarketSnapShot.objects.all().first())

    def create_marketsnapshot(self,marketSnapShotEntity):
        """
        Convert MarketSnapShot Entity To ORMModel & Save It To Database .
        """
        db_snapshot = ORMMarketSnapShot.objects.create(
        totalMarketCapUSD = marketSnapShotEntity.totalMarketCapUSD,
        totalBitcoinMarketCapUSD =  marketSnapShotEntity.bitcoinMarketCapUSD,
        totalAltsMarketCapUSD = marketSnapShotEntity.altsMarketCapUSD,
        bitcoinDominancePer = marketSnapShotEntity.bitcoinDominancePercentage,
        altsDominancePer =marketSnapShotEntity.altsMarketDominancePercentage,
       
        )
        db_snapshot.save()
        return db_snapshot

class MarketChangeRepo:
    """
    This is repository to manage & convert data to and from MarketChageEntity to ORMMarketChage
    """
    def create_marketchange(self,marketChange):
        """
        Convert MarketSnapShot Entity To ORMModel & Save It To Database .
        """
        db_snapshot = ORMMarketChange.objects.create(
        changeInTotalMarketCapPer =marketChange.changeInTotalMarketCapPer,
        changeInTotalMarketCapUSD = marketChange.changeInTotalMarketCapUSD
       
        )
        db_snapshot.save()
        return db_snapshot