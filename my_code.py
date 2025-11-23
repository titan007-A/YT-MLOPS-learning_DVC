import pandas as pd
import os

data = {
    "id": [1,2],
    "name": "Alice",
    "email": "alice@example.com",
    "active": True,
    "roles": ["user", "admin"]
}

df = pd.DataFrame(data)
new_row_loc={"id": 3,
    "name": "Sid",
    "email": "alice@example.com",
    "active": True,
    "roles": "janitor"}
df.loc[len(df.index)]= new_row_loc
print(df.head())
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')


#save the dataframe to a new csv file including column names

df.to_csv(file_path,index=False)

print(f"Csv file saved to {file_path}")
