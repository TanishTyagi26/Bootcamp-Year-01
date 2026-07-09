import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Read datasets
# -----------------------------

inventory = pd.read_csv("inventory_data.csv")
forecast = pd.read_csv("sales_forecast.csv")

# Convert Date column into datetime format
inventory["Date"] = pd.to_datetime(inventory["Date"])
forecast["Date"] = pd.to_datetime(forecast["Date"])

# -----------------------------
# Merge the datasets
# -----------------------------

data = pd.merge(
    inventory,
    forecast,
    on=["Date","SkuID"]
)

# -----------------------------
# Sort according to Date
# -----------------------------

data = data.sort_values("Date")

# -----------------------------
# 7-Day Moving Average
# -----------------------------

data["Demand_MA_7"] = (
    data["ForecastDemand"]
    .rolling(window=7)
    .mean()
)

# -----------------------------
# 30-Day Moving Average
# -----------------------------

data["Demand_MA_30"] = (
    data["ForecastDemand"]
    .rolling(window=30)
    .mean()
)

# -----------------------------
# Stockout Risk
# -----------------------------

data["StockoutRisk"] = (
    data["CurrentStock"] <
    data["SafetyStockLevel"]
)

# -----------------------------
# Restocking Priority
# -----------------------------

conditions = [

    (data["CurrentStock"] <= data["SafetyStockLevel"])
    &
    (data["LeadTime"] >= 7),

    (data["CurrentStock"] <= data["SafetyStockLevel"]),

    (data["CurrentStock"] > data["SafetyStockLevel"])

]

choices = [

    "High",

    "Medium",

    "Low"

]

data["Priority"] = np.select(
    conditions,
    choices,
    default="Low"
)

print(data.head())

# -----------------------------
# Plot
# -----------------------------

plt.figure(figsize=(14,6))

# Step plot
plt.step(
    data["Date"],
    data["CurrentStock"],
    where="mid",
    label="Current Stock"
)

# Safety stock line
plt.axhline(
    y=data["SafetyStockLevel"].mean(),
    color="green",
    linestyle="--",
    label="Average Safety Stock"
)

# Dates where stock below zero
below_zero = data[data["CurrentStock"] < 0]

plt.scatter(
    below_zero["Date"],
    below_zero["CurrentStock"],
    color="red",
    label="Below Zero",
    s=70
)

plt.title("Inventory Stock Level Over Time")

plt.xlabel("Date")

plt.ylabel("Current Stock")

plt.legend()

plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()