# %%
import requests
import pandas as pd
import datetime
import json
import time

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
page = 1
while True:
    response = get_response(page=page, per_page=100, strategy="new")
    print(f'response received {response.status_code}')
    if response.status_code == 200:
        print(f'Saving data for page {page}')
        data = response.json()
        if len(data) < 100:
            break

        save_data(data, 'json')
        page += 1
        time.sleep(2)
    else:
        print(f'Sleeeping')
        time.sleep(10)
