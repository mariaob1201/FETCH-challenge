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

# Reading files
products = pd.read_csv('1_data/PRODUCTS_TAKEHOME.csv', sep=',')

products.groupby('CATEGORY_1').sum()