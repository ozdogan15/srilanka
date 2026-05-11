import pandas as pd
import sys

# grab the files from command line
yieldDataFile = sys.argv[1] 
featureDataFile = sys.argv[2]  
outfile = sys.argv[3]

# reading two files into Pandas as dataFrames
df1 = pd.read_excel(yieldDataFile)
df2 = pd.read_excel(featureDataFile)

# join the two dataframes using merge function by setting how='inner'
# note that we are merging on both distric AND year
output = pd.merge(df1, df2, on=['district','year'], how='inner')

# export the joined result to CSV
output.to_csv(outfile, index=False)

