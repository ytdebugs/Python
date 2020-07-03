import pandas as pd 
import yfinance as yf
import pandas_datareader as pdr
from datetime import date

tickers=['PETR4', 'BBAS3']
start_date='2019-12-30'
end_date=date.today()

def getData(ticker):
    data=pdr.get_data_yahoo(ticker+'.SA', start=start_date, end=end_date)
    print(data)
    data['Ticker']=ticker
    return data

df2=[]

for ticker in tickers:
    print(ticker)
    df1=getData(ticker)
    df1.reset_index(level=0, inplace=True)

# empilhar
    df2.append(df1)

df=pd.concat(df2, ignore_index=True)

df['Adj Close Pct Change']=df.sort_values('Date').groupby(['Ticker'])['Adj Close'].pct_change()
df['Volume Pct Change']=df.sort_values('Date').groupby(['Ticker'])['Volume'].pct_change()

df.to_csv('./acoes_b3.csv', sep=';', decimal=',', encoding='utf-8')






