# List Of Automated Tasks

### Social Media Automation

##### Calculate & Post Market Data SnapShot On Twitter Every Hour .
---
#### Data Sources 
######  Format (ACTION - URL)
-   GET -  https://api.coingecko.com/api/v3/global

----
#### Key Values To Fetch 
-   Total Market Capitalization In USD
-   BTC Dominance
-   ALT Dominance
-   Percentage & Numerical Change In Value of BTC(Mcap) & ALT(Mcap)

[Checkout Tasks File Here](app/automations)


#### Market SnapShot Schema

-   Total_Market_Capitalization_USD : Double
-   BTC_Dominance_Percentage : Double
-   ALTS_Dominance_Percentage : Double
-   BTC_Mcap_USD : Double
-   ALTS_Mcap_USD : Double

[Checkout MarketSnapShot Data Model Here](app/automations/models.py)