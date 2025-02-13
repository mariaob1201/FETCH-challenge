'''
Maria Oros

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
products = pd.read_csv('1_data/raw/PRODUCTS_TAKEHOME.csv', sep=',')
transaction = pd.read_csv('1_data/raw/TRANSACTION_TAKEHOME.csv', sep=',')
user = pd.read_csv('1_data/raw/USER_TAKEHOME.csv', sep=',')

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

#### Console output when running the code

'''
----------------------------------- Products

Products: Total  845552  and Count of NaN in each column relative to the dataset total:
 CATEGORY_1       0.013128
CATEGORY_2       0.168411
CATEGORY_3       7.162895
CATEGORY_4      92.021898
MANUFACTURER    26.784160
BRAND           26.783923
BARCODE          0.476020
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

Transaction: Total  50000  and Count of NaN in each column relative to the dataset total:
 RECEIPT_ID         0.000
PURCHASE_DATE      0.000
SCAN_DATE          0.000
STORE_NAME         0.000
USER_ID            0.000
BARCODE           11.524
FINAL_QUANTITY     0.000
FINAL_SALE         0.000
dtype: float64

Describe 
             BARCODE
count  4.423800e+04
mean   1.715863e+11
std    3.269219e+11
min   -1.000000e+00
25%    3.077212e+10
50%    5.210004e+10
75%    8.536765e+10
max    9.347108e+12

Data types 
 RECEIPT_ID         object
PURCHASE_DATE      object
SCAN_DATE          object
STORE_NAME         object
USER_ID            object
BARCODE           float64
FINAL_QUANTITY     object
FINAL_SALE         object
dtype: object
----------------------------------- User

User: Total  100000  and Count of NaN in each column relative to the dataset total:
 ID               0.000
CREATED_DATE     0.000
BIRTH_DATE       3.675
STATE            4.812
LANGUAGE        30.508
GENDER           5.892
dtype: float64

Describe 
                               ID               CREATED_DATE                 BIRTH_DATE  STATE LANGUAGE  GENDER
count                     100000                     100000                      96325  95188    69492   94108
unique                    100000                      99942                      54721     52        2      11
top     5ef3b4f17053ab141787697d  2023-01-12 18:30:15.000 Z  1970-01-01 00:00:00.000 Z     TX       en  female
freq                           1                          2                       1272   9028    63403   64240

Data types 
 ID              object
CREATED_DATE    object
BIRTH_DATE      object
STATE           object
LANGUAGE        object
GENDER          object
dtype: object
'''

## First thoughts
''' 
- First assessment - Are there any data quality issues present?
    Products:
    From 1-4 categories, the Category 4 has 92% of the total data as missing, wonder if it is an issue on how the data is captured or nature of the business eg no standard categorization of item at that level
    Barcode has missings .047% of missings: this is relevant because bar code matches wuth Products table, in such case as as those are few, need to be excluded when merging tables
    Manufacturer and brand are also with missing information (26% of the data): relevant if a research question is about that information
    
    User: 
    mostly categorical information: demographics and ID:
    ID, CREATED_DATE with 0.000% missings which is great to have track of the users since their first registration
    LANGUAGE        30.508% missings, refrain on its usage later
    BIRTH_DATE, STATE ,GENDER, less than <6% missings 
    
    Transaction: 
    seems to be the data set with more complete data, the only field with missing information is BARCODE about 11% onf the total entries
    FINAL_QUANTITY and FINAL_SALE are not numeric
    
    Other data quality issues are reatives to the data types, eg FINAL_QUANTITY and FINAL_SALE were not numerical data as it was described in the entity relationship model. 
    The same occurred with date.

- Are there any fields that are challenging to understand?
    Not really. seems like there were some inconsistencies in the data that lead into a difficult intepretation for example in
    transactions table FINAL_SALE some times reported missing but FINAL_QUANTITY is not missing in the same observation. 
'''

