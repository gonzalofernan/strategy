import yfm 
import pandas as pd 
import datetime

# Get list of S&P 500 tickers 

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0] 
list=df['Symbol'].tolist()


# Fetcher 
fetcher = yfm.fetcher() 
start= str(datetime.datetime.now() - datetime.timedelta(days=365))

# Bucle para añadir  
for ticker in list:
    fetcher.add(symbol=ticker) # yyyy/mm/dd

#fetcher.add("")

