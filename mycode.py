import pandas as pd
import os

# Sample dataframe with column names
data = {
    'Name' : ['Devansh','Rajani','Deva'],
    'Age' : [20,21,22],
    'City' : ['Rajkot','Ahmedabad','Surat']
}

df = pd.DataFrame(data)

new_row_loc = {'Name':'Shiv','Age':22, 'City':'Rajkot'}
df.loc[len(df.index)] = new_row_loc

new_row_loc2 = {'Name':'Vishnu','Age':'23','City':'Rajkot'}
df.loc[len(df.index)] = new_row_loc2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample.csv')

df.to_csv(file_path,index=False)
