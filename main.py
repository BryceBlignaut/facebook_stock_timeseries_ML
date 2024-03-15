#%%
import requests
import pandas as pd
import json


#%%
api_key = "GMD3FCDBVUY681WT"

# import the data
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=META&outputsize=full&apikey={api_key}'
r = requests.get(url)
data = r.json()
print(data)
# %%
df = pd.json_normalize(data)
df = pd.
#%%
df.head(5)
# %%
