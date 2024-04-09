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

# %%
df.to_csv('data.csv')
# %%
# Functions and process - New Script
def call_api(ticker, api_key):
    # Fetching data from the API
    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={api_key}'
    try:
        response = requests.get(api_url)
        data = response.json()

        # Extracting the time series data
        time_series = data["Time Series (Daily)"]

        # Converting the data into a pandas DataFrame
        df = pd.DataFrame(time_series).T.reset_index()
        df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
        df["Date"] = pd.to_datetime(df["Date"])
        df[["Open", "High", "Low", "Close"]] = df[["Open", "High", "Low", "Close"]].astype(float)
        df = df.sort_values(by="Date",ascending=False)

        return {'ticker': ticker, 'data': df}
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
    
def process_tickers(tickers, filename):
    api_data = []
    for ticker in tickers:
        api_data.append(call_api(ticker, api_key))
    
    df = pd.DataFrame(api_data)
    
    # Append to CSV
    try:
        existing_data = pd.read_csv(filename)
        df.to_csv(filename, mode='a', header=False, index=False)
    except FileNotFoundError:
        df.to_csv(filename, index=False)

tickers = ['AAPL', 'GOOGL', 'MSFT','META']
filename = 'data.csv'
api_key = "GMD3FCDBVUY681WT"
process_tickers(tickers, filename)

#%%
df = pd.read_csv('data.csv')

df.head()
# %%
df.tail(50)
# %%
