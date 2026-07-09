import pandas as pd
import numpy as np

np.random.seed(42)

# Number of days
days = 120

dates = pd.date_range("2025-01-01", periods=days)

inventory = pd.DataFrame({
    "Date": dates,
    "SkuID": np.random.choice(["SKU101","SKU102","SKU103"], days),
    "WarehouseID": np.random.choice(["WH1","WH2"], days),
    "CurrentStock": np.random.randint(-20,250,days),
    "SafetyStockLevel": np.random.randint(30,80,days),
    "DailyReorderQuantity": np.random.randint(20,100,days)
})

sales_forecast = pd.DataFrame({
    "Date": dates,
    "SkuID": inventory["SkuID"],
    "ForecastDemand": np.random.randint(10,80,days),
    "LeadTime": np.random.randint(2,10,days)
})

inventory.to_csv("inventory_data.csv",index=False)
sales_forecast.to_csv("sales_forecast.csv",index=False)

print("Datasets Generated Successfully")