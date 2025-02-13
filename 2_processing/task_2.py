'''
Maria Oros
Second: provide SQL queries

Answer three of the following questions with at least one question coming from the closed-ended and one from the open-ended question set. Each question should be answered using one query.

Closed-ended questions:

What are the top 5 brands by receipts scanned among users 21 and over?
What are the top 5 brands by sales among users that have had their account for at least six months?
What is the percentage of sales in the Health & Wellness category by generation? (*)

Open-ended questions: for these, make assumptions and clearly state them when answering the question.

Who are Fetch’s power users?
Which is the leading brand in the Dips & Salsa category? (*)
At what percent has Fetch grown year over year? (*)
'''

import pandas as pd
import numpy as np

# Reading files
users_transactions = pd.read_csv('/Users/mariaoros/Documents/Github-projects/2025/Fetch-DataAnalystHome/1_data/processed/users_transactions_inner.csv', sep=',')
products_transactions = pd.read_csv('/Users/mariaoros/Documents/Github-projects/2025/Fetch-DataAnalystHome/1_data/processed/products_transactions_inner.csv', sep=',')


print(users_transactions.columns)
print(users_transactions.dtypes)
########################## Q1: What are the top 5 brands by sales among users that have had their account for at least six months?
# I am assuming
#   that receipts scanned mean the number of receipt_id's and
# This mean getting the data from transactions, users and products, will use the merged data from eda.ipynb

#summ=users_transactions[users_transactions['TIME_AS_USER_WHEN_PURCHASING_MO']>6].groupby('BRAND')['FINAL_SALE'].sum().reset_index()
#print(summ)
######################################## MERGING


merged_df.to_csv('../1_data/processed/merged_data.csv')
