''' SCRIPT 3
Maria Oros
This is the assessment of the data in terms of simple stats of the fields, to evaluate consistency and completitude of the information
AFTER cleaning the datasets


------- Instructions from link --------
First: explore the data

Review the unstructured csv files and answer the following questions with code that supports your conclusions:

Are there any data quality issues present?
Are there any fields that are challenging to understand?
We recommend using SQL or python and data visualization to examine the data.

----- to run this code you can do from terminal:
python 2_processing/1_explore_data.py run
'''

import pandas as pd
import numpy as np

# Reading files
products = pd.read_parquet('1_data/processed/PRODUCTS_TAKEHOME_clean.parquet')
transaction = pd.read_parquet('1_data/processed/TRANSACTION_TAKEHOME_clean.parquet')
user = pd.read_csv('1_data/processed/USER_TAKEHOME_clean.csv', sep=',')

# Data Exploration step 1: Checking for missing values and data stats description
print("----------------------------------- Products")
print("\nProducts: Total ", len(products), " and Count of NaN in each column relative to the dataset total:\n", 100*products.isnull().sum()/len(products))
print("\nDescribe \n", products.describe())
print("\nData types \n", products.dtypes)

print("----------------------------------- Transaction")
print("\nTransaction: Total ", len(transaction), " and Count of NaN in each column relative to the dataset total:\n", 100*transaction.isnull().sum()/len(transaction))
print("\nDescribe \n", transaction.describe())
print("\nData types \n", transaction.dtypes)

print("----------------------------------- User")
print("\nUser: Total ", len(user), " and Count of NaN in each column relative to the dataset total:\n", 100*user.isnull().sum()/len(user))
print("\nDescribe \n", user.describe())
print("\nData types \n", user.dtypes)

'''
----------------------------------- Products

Products: Total  841527  and Count of NaN in each column relative to the dataset total:
 CATEGORY_1       0.013190
CATEGORY_2       0.078548
CATEGORY_3       6.977079
CATEGORY_4      92.010239
MANUFACTURER    26.882916
BRAND           26.882679
BARCODE          0.000000
dtype: float64

Describe 
             BARCODE
count  8.415270e+05
mean   6.016109e+11
std    1.022530e+12
min    1.850000e+02
25%    7.124923e+10
50%    6.344185e+11
75%    7.683955e+11
max    6.291108e+13

Data types 
 CATEGORY_1       object
CATEGORY_2       object
CATEGORY_3       object
CATEGORY_4       object
MANUFACTURER     object
BRAND            object
BARCODE         float64
dtype: object
----------------------------------- Transaction

Transaction: Total  44238  and Count of NaN in each column relative to the dataset total:
 RECEIPT_ID                0.0
PURCHASE_DATE             0.0
SCAN_DATE                 0.0
STORE_NAME                0.0
USER_ID                   0.0
BARCODE                   0.0
FINAL_QUANTITY            0.0
FINAL_SALE                0.0
FINAL_QUANTITY_NUMERIC    0.0
FINAL_SALE_NUMERIC        0.0
PURCHASE_DATE_CT          0.0
dtype: float64

Describe 
             BARCODE  FINAL_QUANTITY_NUMERIC  FINAL_SALE_NUMERIC
count  4.423800e+04            44238.000000        44238.000000
mean   1.715863e+11                0.814877            3.413256
std    3.269219e+11                1.944923            4.655831
min   -1.000000e+00                0.000000            0.000000
25%    3.077212e+10                0.000000            0.000000
50%    5.210004e+10                1.000000            2.270000
75%    8.536765e+10                1.000000            4.490000
max    9.347108e+12              276.000000           81.810000

Data types 
 RECEIPT_ID                             object
PURCHASE_DATE                          object
SCAN_DATE                              object
STORE_NAME                             object
USER_ID                                object
BARCODE                               float64
FINAL_QUANTITY                         object
FINAL_SALE                             object
FINAL_QUANTITY_NUMERIC                float64
FINAL_SALE_NUMERIC                    float64
PURCHASE_DATE_CT          datetime64[ns, UTC]
dtype: object
----------------------------------- User

User: Total  100000  and Count of NaN in each column relative to the dataset total:
 Unnamed: 0          0.000
ID                  0.000
CREATED_DATE        0.000
BIRTH_DATE          0.000
STATE               4.812
LANGUAGE           30.508
GENDER              5.892
BIRTH_DATE_FIX      3.675
CREATED_DATE_CT     0.000
dtype: float64

Describe 
           Unnamed: 0
count  100000.000000
mean    49999.500000
std     28867.657797
min         0.000000
25%     24999.750000
50%     49999.500000
75%     74999.250000
max     99999.000000

Data types 
 Unnamed: 0          int64
ID                 object
CREATED_DATE       object
BIRTH_DATE         object
STATE              object
LANGUAGE           object
GENDER             object
BIRTH_DATE_FIX     object
CREATED_DATE_CT    object
dtype: object
'''

## Data seems to be much better in terms of quality
# The issue clear is barcode =-1 which can be mistakenly gathered from the process of the transaction
# or a default value for certain items, might be a need to delete it