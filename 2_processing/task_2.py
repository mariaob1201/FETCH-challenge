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
merged_df = pd.read_csv('../1_data/processed/snapshot_021325.csv')

print(merged_df.columns)
print(merged_df.dtypes)
########################## Q1: What are the top 5 brands by sales among users that have had their account for at least six months?
# I am assuming
#   that receipts scanned mean the number of receipt_id's and
# This mean getting the data from transactions, users and products, will use the merged data from eda.ipynb

#summ=users_transactions[users_transactions['TIME_AS_USER_WHEN_PURCHASING_MO']>6].groupby('BRAND')['FINAL_SALE'].sum().reset_index()
#print(summ)
######################################## MERGING


merged_df["BIRTH_DATE"] = pd.to_datetime(merged_df['BIRTH_DATE'], errors='coerce')
merged_df["CREATED_DATE"] = pd.to_datetime(merged_df['CREATED_DATE'], errors='coerce')

# create AGE_WHEN_CREATION years between birth date and date of creation both from USERS table
merged_df['AGE_WHEN_CREATION'] = merged_df.apply(
    lambda row: np.floor((row['CREATED_DATE'] - row['BIRTH_DATE']).days / 365.25)
    if pd.notnull(row['CREATED_DATE']) and pd.notnull(row['BIRTH_DATE']) else np.nan,
    axis=1
)

merged_df['PURCHASE_DATE_CT'] = pd.to_datetime(merged_df['PURCHASE_DATE'])
merged_df['PURCHASE_DATE_CT'] = merged_df['PURCHASE_DATE_CT'].dt.tz_localize('UTC')


merged_df['TIME_AS_USER_WHEN_PURCHASING'] = merged_df.apply(
    lambda row: np.floor((row['PURCHASE_DATE_CT'] - row['CREATED_DATE']).days / 365.25)
    if pd.notnull(row['PURCHASE_DATE_CT']) and pd.notnull(row['CREATED_DATE']) else np.nan,
    axis=1
)

merged_df['TIME_AS_USER_WHEN_PURCHASING_MO'] = merged_df.apply(
    lambda row: np.floor((row['PURCHASE_DATE_CT'] - row['CREATED_DATE']).days / 30.4375)
    if pd.notnull(row['PURCHASE_DATE_CT']) and pd.notnull(row['CREATED_DATE']) else np.nan,
    axis=1
)

print(len(merged_df))
