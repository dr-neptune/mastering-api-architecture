import sqlite3
import yfinance as yf
import pandas as pd

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('market_data.db')

# Create a list of S&P 500 stock symbols
sp500_symbols = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'TSLA', 'NVDA', 'JPM', 'JNJ']

# Create an empty list to store the data
market_data = []

# Fetch market data for each stock symbol
for symbol in sp500_symbols:
    print(f"working on {symbol}")
    # Download historical data for the stock
    stock_data = yf.download(symbol, start='2022-01-01', end='2024-01-01').reset_index()

    # Add the stock symbol as a new column
    stock_data['Symbol'] = symbol

    # Append the stock data to the market_data list
    market_data.append(stock_data)

# Concatenate all the stock data into a single DataFrame
market_df = pd.concat(market_data, ignore_index=True)

market_df = market_df.reset_index().rename(columns={'index': 'id', 'Adj Close': 'Adj_Close'})

# Write the DataFrame to the SQLite database
market_df.to_sql('market_data', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
