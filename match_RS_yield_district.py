# the purpose of this python script is to merge yield prediction features
# extracted from GEE with district-level yield data to be used in the RF algorithm

import pandas as pd
  
# reading extracted features from GEE as a CSV file
# must have district and year columns present
df1 = pd.read_csv('your GEE extracted features goes here')

# reading clean district-level yield data in excel format
# must have district and year columns
df2 = pd.read_excel('LK_maha_yield_clean_2010_2024.xlsx')
#df2 = pd.read_excel('LK_yala_yield_clean_2010_2024.xlsx')

# using merge function by setting how='inner'
output = pd.merge(df1, df2, on=['district','year'], how='inner')
  
# export merged results to a csv file
output.to_csv('LK_maha_yield_clean_features_2010_2024.csv', index=False)
#output.to_csv('LK_yala_yield_clean_features_2010_2024.csv', index=False)

