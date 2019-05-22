import pandas as pd 
path = './data/database.csv'
data = pd.read_csv(path)
# print(data.info())
# print(data.head())
for i in data.index.values:
    row = data.iloc[i]
    id, name, phone = row['id'], row['name'], row['phone']
    print('{}_{}_{}'.format(id, name, phone))