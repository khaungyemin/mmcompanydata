import pandas as pd
from pandas.io.json import json_normalize
import glob
import csv
import shutil

path = r'F:\Myanmar_Financials\re-master' # use your path
all_files = glob.glob(path + "\*.json")
data=[]
f = open('F:\Myanmar_Financials\company_master.csv', 'w')
writer = csv.writer(f)
for file in all_files:
    print(file)
    data = pd.read_json(file, lines=True)
    crop = data["Corp"]
    for raw in crop:
        data = [raw["CompanyName"] ,raw["IsForeign"],raw["RegistrationDate"]]
    writer.writerow(data)
    print(file)
    print(data)
    shutil.move(f"{file}",r'F:\Myanmar_Financials\done')
f.close()