import pandas as pd
from pathlib import Path
import re
import sys
import os

def parse():
    file = sys.argv[1]
    filename, file_extension = os.path.splitext(file)
    outname = Path(file).stem

    read_file = pd.read_excel(file)

    read_file.to_csv (filename + ".csv",
                      index = None,
                      header=True)

    df = pd.DataFrame(pd.read_csv(filename + ".csv"))

    newcol = [(re.search('\(.*\)', str(x))).group() for x in df['Sample_ID']]
    df.insert(1,"Transition", newcol)
    
    df['Sample_ID'] = [re.sub('\+.*\)\s', '', str(x)) for x in df['Sample_ID']]
    df['Sample_ID'] = [re.sub('\s\s.*', '', str(x)) for x in df['Sample_ID']]
    df['Sample_ID'] = [re.sub('\s', '', str(x)) for x in df['Sample_ID']]

    os.remove(filename + ".csv")
    os.makedirs("./parsed", exist_ok=True)
    df.to_csv("./parsed/" + outname + ".csv", sep=',', encoding='utf-8', index=False)

if __name__ == '__main__':
    parse()
