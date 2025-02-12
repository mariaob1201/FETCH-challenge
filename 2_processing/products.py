import pandas as pd

# Reading files
products = pd.read_csv('1_data/PRODUCTS_TAKEHOME.csv', sep=',')

products.groupby('CATEGORY_1').sum()