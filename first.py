import pandas as pd

# Read dataset using pandas function with parse_dates to handle Date column as datetime
dataset = pd.read_csv("gold_price_data.csv", parse_dates=["Date"])
