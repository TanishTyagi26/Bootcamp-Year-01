import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


# Number of tick records
records = 50000


# Stocks
tickers = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "TSLA"
]


# Starting prices
base_prices = {
    "AAPL": 189,
    "MSFT": 420,
    "GOOGL": 175,
    "TSLA": 250
}


start_time = datetime(
    2026,
    1,
    1,
    9,
    30,
    0
)


data = []


current_prices = base_prices.copy()



for i in range(records):

    # Increasing timestamp
    timestamp = start_time + timedelta(
        seconds=i
    )


    ticker = random.choice(
        tickers
    )


    action = random.choice(
        [
            "Buy",
            "Sell"
        ]
    )


    # Random walk price movement
    movement = np.random.normal(
        0,
        0.15
    )


    current_prices[ticker] += movement


    price = round(
        current_prices[ticker],
        2
    )


    # Random volume with occasional spikes

    if random.random() < 0.05:
        volume = random.randint(
            10000,
            50000
        )
    else:
        volume = random.randint(
            100,
            5000
        )


    data.append(
        [
            timestamp,
            ticker,
            action,
            price,
            volume
        ]
    )



# Create DataFrame

df = pd.DataFrame(
    data,
    columns=[
        "Timestamp",
        "Ticker",
        "Action",
        "Price",
        "Volume"
    ]
)



# Save file

df.to_csv(
    "orders.csv",
    index=False
)


print("Large orders.csv created!")
print("Rows:", len(df))
print(df.head())