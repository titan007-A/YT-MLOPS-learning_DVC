import pandas as pd
import os

data = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "active": True,
    "roles": ["user", "admin"]
}

df = pd.DataFrame(data)
df2= pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')


#save the dataframe to a new csv file including column names

df.to_csv(file_path,index=False)

print(f"Csv file saved to {file_path}")
