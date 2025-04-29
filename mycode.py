import pandas as pd
import os

# Sample dataframe with column names
data = {
    'Name' : ['Devansh','Rajani','Deva'],
    'Age' : [20,21,22],
    'City' : ['Rajkot','Ahmedabad','Surat']
}

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample.csv')

df.to_csv(file_path,index=False)
