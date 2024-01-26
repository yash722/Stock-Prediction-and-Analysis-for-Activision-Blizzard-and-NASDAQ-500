# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

ticker="atvi"

input_dir = os.getcwd()
root_dir = os.getcwd()
plot_dir =os.path.join(input_dir, ticker + "_weekly_plots")
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)
ticker_file = os.path.join(input_dir, ticker + '_weekly_return_detailed.csv')

try:   
    df = pd.read_csv(ticker_file)
    for i in range(1, len(df)-10, 10): 
        first_date = df["Date"].iloc[i]
        last_date  = df["Date"].iloc[i+10]
        next_df = df.loc[(df["Date"]>=first_date) & (df["Date"]<=last_date)]
        fig = plt.figure()
        ax = plt.gca()
        df_1 = next_df[['Date','Week_Number','Weekday', 'Day', 'Adj Close']]
        weekday_list = df_1['Weekday'].tolist()
        ticks_list   = df_1['Date'].tolist()
        plt.plot(df_1['Date'], df_1['Adj Close'])
        plt.xticks(ticks_list, weekday_list, rotation=45)
        plt.grid(True)
        plt.title('daily prices for ' + ticker +  ' from ' + first_date + ' to ' + last_date)
        output_file = os.path.join(plot_dir, ticker + '_prices_' + i +  '.pdf')
#        plt.show()
        print("generated " + output_file)
        fig.tight_layout()
        fig.savefig(output_file)
    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)













