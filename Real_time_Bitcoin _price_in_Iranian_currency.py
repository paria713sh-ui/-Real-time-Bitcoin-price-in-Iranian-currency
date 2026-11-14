# Real time Bitcoin price in Iranian currency
import requests
dollar=0
url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur"
data=requests.get(url)
if data.status_cod==200:
 bitcoin=data.json()
 dollar=bitcoin["bitcoin"]["usd"]
 dollar_toman=dollar*230000
 print(bitcoin ,end="")
 print(f"toman={dollar_toman}")
else:
 print("check your Internet")






        