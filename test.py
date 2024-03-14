#%%
import requests
import pandas as pd

# Fetching data from the API
api_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=META&outputsize=full&apikey={api_key}"

response = requests.get(api_url)
data = response.json()

# Extracting the time series data
time_series = data["timestamp"]

# Converting the data into a pandas DataFrame
df = pd.DataFrame(time_series).T.reset_index()
df.columns = ["timestamp", "open", "high", "low", "close","volume"]

# Ensuring proper data types
df["timestamp"] = pd.to_datetime(df["timestamp"])
df[["timestamp","open", "high", "low", "close"]] = df[["Open", "High", "Low", "Close"]].astype(float)

# Sorting DataFrame by Date
df = df.sort_values(by="timestamp")

print(df.head())
# %%
