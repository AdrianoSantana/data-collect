# %%
import requests
import pandas as pd
import datetime
import json

def get_response(**kwargs):
    url = "https://www.tabnews.com.br/api/v1/contents"
    return requests.get(url, params=kwargs)

def save_data(data, option='json'):
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')
    path_save = f'../data/raw/contents/{option}'
    if option == 'json':
        with open(f'{path_save}/{now}.json', 'w') as open_file:
            json.dump(data, open_file, indent=4)
    elif option == 'dataframe':
        df = pd.DataFrame(data)
        df.to_parquet(f'{path_save}/{now}.parquet', index=False)
        
            
# %%
response = get_response(page=1, per_page=100, strategy="new")
data = response.json()
# %%
save_data(data, 'json')