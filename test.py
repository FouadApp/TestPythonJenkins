import csv
import pandas as pd
df = pd.read_csv('client.csv')
#print (df.acount.count())
print (df.describe())
dfDescribe = df.describe()
dfDescribe.to_csv('clientsDescribe.csv')

