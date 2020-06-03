# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:06:06 2020
@author: Manish Sharma
www.RebellionRider.com
www.instagram.com/RebellionRider
www.YouTube.com/RebellionRider
"""

import pandas as pd
import requests

#Step 1 Data Collection
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic'
req = requests.get(url)
data_list = pd.read_html(req.text)
target_df = data_list[4]

#Step 2 Data Cleaning
#Issue 1 Column Names
target_df.columns = ['Col0','Country Name','Total Cases','Total Deaths','Total Recoveries','Col5']
#Issue 2 Extra Columns
target_df = target_df[['Country Name','Total Cases','Total Deaths','Total Recoveries']]
#Issue 3 Extra Rows
#target_df = target_df.drop([229, 228])
last_idx = target_df.index[-1]
target_df = target_df.drop([last_idx, last_idx-1])
#Issue 4 Inconsistent Country Name
target_df['Country Name'] = target_df['Country Name'].str.replace('\[.*\]','')
#Issue 5 Extra Value ("No Data") in Column 4
target_df['Total Recoveries'] = target_df['Total Recoveries'].str.replace('No data','0')
#Issue 6 Wrong Data Type
target_df['Total Cases'] = pd.to_numeric(target_df['Total Cases'])
target_df['Total Deaths'] = pd.to_numeric(target_df['Total Deaths'])
target_df['Total Recoveries'] = pd.to_numeric(target_df['Total Recoveries'])

#Step 3 Export The Data
#target_df.to_csv(r'covid19_dataset.csv')
target_df.to_excel(r'covid19_dataset.xlsx')

