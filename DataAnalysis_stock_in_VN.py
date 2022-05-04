# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:46:30 2022

@author: ACER
"""
#Import libraries
import pandas as pd
import numpy as np
import datetime as dt #Handle with datetime data
#!pip install investpy
import investpy #Load stock's data
import seaborn as sns
import matplotlib.pyplot as plt

#Set up start/end date
start = "01/01/2021"
end  = dt.datetime.now().strftime("%d/%m/%Y")

#Load dataset of 3 banks: CTG, ACB, VCB
CTG = investpy.get_stock_historical_data(stock= "CTG", country= 'vietnam', 
                                         from_date = start, to_date = end)              
CTG.drop("Currency", axis = 1, inplace = True)

ACB = investpy.get_stock_historical_data(stock= "ACB", country= 'vietnam', 
                                         from_date = start, to_date = end)
ACB.drop("Currency", axis = 1, inplace = True)


VCB = investpy.get_stock_historical_data(stock= "VCB", country= 'vietnam', 
                                         from_date = start, to_date = end)                                  
VCB.drop("Currency", axis = 1, inplace = True)

#Create the table that has full information of stocks's price
list_banks = ['CTG', 'ACB', 'VCB'] # Mark which dataframe the information comes from
bank_stocks = pd.concat([CTG,ACB,VCB],axis=1, keys = list_banks)
bank_stocks.columns.names = ['Bank Name','Stock Info'] #Set name for columns
#Check missing value
bank_stocks.isna().sum()

#Find the highest close price of each stock
bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()

#Find rate of return of each stock
value_banks = pd.DataFrame()
for name in list_banks:
    value_banks[name+' Rate_of_return'] = bank_stocks[name]['Close'].pct_change()
    
#Handle with missing value on the first day
value_banks.dropna(inplace= True)

# Visualization
sns.pairplot(value_banks)

plt.figure(figsize=(15,5)) # Tùy chỉnh kích thước biểu đồ
sns.distplot(value_banks.loc['2021-01-01':'2021-12-31']['ACB Rate_of_return'],
             color='green',bins=100)




