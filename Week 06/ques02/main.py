import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# ==========================================================
# 1. LOAD DATA
# ==========================================================

df = pd.read_csv("orders.csv")


df["Timestamp"] = pd.to_datetime(
    df["Timestamp"]
)


df = df.sort_values(
    "Timestamp"
)


print(df.head())


# ==========================================================
# 2. VWAP CALCULATION (5 MIN WINDOW)
# ==========================================================


def calculate_vwap(group):

    volume = group["Volume"].sum()

    if volume == 0:
        return np.nan

    return (
        (group["Price"] * group["Volume"]).sum()
        /
        volume
    )



vwap = (
    df.groupby(
        [
            "Ticker",
            pd.Grouper(
                key="Timestamp",
                freq="5min"
            )
        ]
    )
    .apply(calculate_vwap)
    .reset_index(name="VWAP")
)



# ==========================================================
# 3. BID ASK SPREAD
# ==========================================================


def calculate_spread(group):

    bid = group.loc[
        group["Action"] == "Buy",
        "Price"
    ].max()


    ask = group.loc[
        group["Action"] == "Sell",
        "Price"
    ].min()



    if pd.isna(bid) or pd.isna(ask):
        return np.nan


    return ask - bid



spread = (
    df.groupby(
        [
            "Ticker",
            pd.Grouper(
                key="Timestamp",
                freq="5min"
            )
        ]
    )
    .apply(calculate_spread)
    .reset_index(name="Spread")
)



microstructure = pd.merge(
    vwap,
    spread,
    on=[
        "Ticker",
        "Timestamp"
    ]
)



print("\nMarket Microstructure")
print(microstructure.head())



# ==========================================================
# 4. NUMPY MARKET DEPTH (10 PRICE LEVELS)
# ==========================================================


stock = "AAPL"


stock_data = df[
    df["Ticker"] == stock
]


prices = stock_data[
    "Price"
].to_numpy()


volumes = stock_data[
    "Volume"
].to_numpy()



current_price = prices[-1]



price_levels = np.linspace(
    current_price - 5,
    current_price + 5,
    10
)



# Sort prices for fast searching

idx = np.argsort(prices)


sorted_prices = prices[idx]

sorted_volumes = volumes[idx]



depth = []



for level in price_levels:

    left = np.searchsorted(
        sorted_prices,
        level - 0.05
    )


    right = np.searchsorted(
        sorted_prices,
        level + 0.05
    )


    depth.append(
        sorted_volumes[left:right].sum()
    )



depth = np.array(depth)



print("\nMarket Depth")

for p, d in zip(price_levels, depth):

    print(
        f"{p:.2f} : {d}"
    )



# ==========================================================
# 5. CREATE OHLC CANDLES
# ==========================================================


ohlc = (
    stock_data
    .set_index("Timestamp")
    .resample("5min")
    .agg(
        Open=("Price","first"),
        High=("Price","max"),
        Low=("Price","min"),
        Close=("Price","last"),
        Volume=("Volume","sum")
    )
)


ohlc.dropna(
    inplace=True
)



print("\nOHLC DATA")
print(ohlc.head())



# ==========================================================
# 6. PREPARE VWAP FOR SELECTED STOCK
# ==========================================================


stock_vwap = vwap[
    vwap["Ticker"] == stock
]



# ==========================================================
# 7. PLOT CANDLESTICK + VWAP + VOLUME
# ==========================================================


fig, (
    price_ax,
    volume_ax
) = plt.subplots(
    2,
    1,
    figsize=(18,10),
    sharex=True,
    gridspec_kw={
        "height_ratios":[3,1]
    }
)



# Convert dates

dates = mdates.date2num(
    ohlc.index.to_pydatetime()
)



# -------------------------------
# Candlestick chart
# -------------------------------


for date, (_, row) in zip(
        dates,
        ohlc.iterrows()
):


    color = (
        "green"
        if row["Close"] >= row["Open"]
        else "red"
    )



    # wick

    price_ax.plot(
        [
            date,
            date
        ],
        [
            row["Low"],
            row["High"]
        ],
        color=color,
        linewidth=1
    )



    # body

    price_ax.bar(
        date,
        abs(
            row["Close"]
            -
            row["Open"]
        ),
        bottom=min(
            row["Open"],
            row["Close"]
        ),
        width=0.0025,
        color=color,
        edgecolor=color
    )



# VWAP line

price_ax.plot(
    stock_vwap["Timestamp"],
    stock_vwap["VWAP"],
    color="blue",
    linewidth=2,
    label="VWAP"
)



price_ax.set_title(
    f"{stock} High Frequency Order Book Reconstruction"
)


price_ax.set_ylabel(
    "Price"
)


price_ax.legend()



# -------------------------------
# Volume spikes
# -------------------------------


volume_ax.bar(
    ohlc.index,
    ohlc["Volume"],
    color="orange"
)


volume_ax.set_ylabel(
    "Volume"
)



volume_ax.xaxis.set_major_formatter(
    mdates.DateFormatter(
        "%H:%M"
    )
)



plt.xticks(
    rotation=45
)


plt.tight_layout()

plt.show()