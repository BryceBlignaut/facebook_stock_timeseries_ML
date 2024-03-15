#%%
import requests
import pandas as pd

# Fetching data from the API
api_key = "GMD3FCDBVUY681WT"
api_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=META&outputsize=full&apikey={api_key}"

response = requests.get(api_url)
data = response.json()

# Extracting the time series data
time_series = data["Time Series (Daily)"]

# Converting the data into a pandas DataFrame
df = pd.DataFrame(time_series).T.reset_index()
#%%
df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
# %%
df["Date"] = pd.to_datetime(df["Date"])
# %%
df[["Open", "High", "Low", "Close"]] = df[["Open", "High", "Low", "Close"]].astype(float)
# %%
df = df.sort_values(by="Date",ascending=False)

df.head()
# %%
