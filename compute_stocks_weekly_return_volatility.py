# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:37:48 2019

@author: epinsky
"""

# run this  !pip install pandas_datareader
# from pandas_datareader import data as web
import os
import math
import numpy as np 
import pandas as pd
import yfinance as yf

ticker='spy'

input_dir = os.getcwd()
output_file = os.path.join(input_dir, ticker + '_weekly_return_volatility.csv')

try:
    df = yf.download(ticker, start="2018-01-01", end="2022-12-31")
    df['Return'] = df['Adj Close'].pct_change()
    df['Return'].fillna(0, inplace = True)
    df['Return'] = 100.0 * df['Return']
    df['Return'] = df['Return'].round(3)        
    df['Date'] = df.index
    df['Date'] = pd.to_datetime(df['Date'])
    df['Week_Number'] = df['Date'].dt.strftime('%U')
    df['Year'] = df['Date'].dt.year 
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.day_name()
    df_2 = df[['Year', 'Week_Number', 'Return']]
    df_2.index = range(len(df))
    df_grouped = df_2.groupby(['Year', 'Week_Number'])['Return'].agg([np.mean, np.std])
    df_grouped.reset_index(['Year', 'Week_Number'], inplace=True)
    df_grouped.rename(columns={'mean': 'mean_return', 'std':'volatility'}, inplace=True)
    df_grouped.fillna(0, inplace=True)
    df_grouped.to_csv(output_file, index=False)
    print("wrote ", len(df_grouped), " lines to file: ", output_file)

#    df_grouped_2 = df_grouped.fillna(0)
#    df_grouped_2.to_csv(output_file, index=False)
    
except Exception as e:
    print(e)


output_file = os.path.join(input_dir, ticker + '_weekly_return_detailed.csv')
combined_df = df.merge(df_grouped, on=['Year', 'Week_Number'], how = 'inner')
combined_df.to_csv(output_file, index=False)
print("\n wrote ", len(combined_df), " lines to file to ", output_file)







