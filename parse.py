import pandas as pd
import re
import sys
import os

file = sys.argv[1]
filename, file_extension = os.path.splitext(file)
outname = os.path.join('./', filename + '.csv')

read_file = pd.read_excel(file)
  
read_file.to_csv (filename + ".csv", 
                  index = None,
                  header=True)

df = pd.DataFrame(pd.read_csv(filename + ".csv"))

df['Sample_ID'] = [re.sub('\+.*\)\s', '', str(x)) for x in df['Sample_ID']]

df['Sample_ID'] = [re.sub('\s\s.*', '', str(x)) for x in df['Sample_ID']]

df.to_csv(filename + ".csv", sep=',', encoding='utf-8', index=False)

