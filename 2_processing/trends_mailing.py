'''
Maria Oros
Third: communicate with stakeholders
Construct an email or slack message that is understandable to a product or business leader who is not familiar with your day-to-day work. Summarize the results of your investigation. Include:

Key data quality issues and outstanding questions about the data
One interesting trend in the data
Use a finding from part 2 or come up with a new insight
Request for action: explain what additional help, info, etc. you need to make sense of the data and resolve any outstanding issues
'''

import pandas as pd
import numpy as np

# Reading files
merged_df = pd.read_parquet('1_data/processed/snapshot_021325.csv')

print(merged_df.columns)
print(merged_df.dtypes)


