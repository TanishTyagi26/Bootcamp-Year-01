import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of transactions
n = 10000

# Generate data
invoice_numbers = np.random.randint(100000, 999999, n)
customer_ids = np.random.randint(10000, 10250, n)
stock_codes = np.random.choice(
    ['A100', 'B200', 'C300', 'D400', 'E500', 'F600', 'G700'],
    n
)

quantities = np.random.randint(1, 20, n)
unit_prices = np.round(np.random.uniform(1.5, 150.0, n), 2)

# Random dates between Jan and Dec 2023
invoice_dates = pd.to_datetime("2023-01-01") + pd.to_timedelta(
    np.random.randint(0, 365, n),
    unit="D"
)

# Create DataFrame
online_retail = pd.DataFrame({
    "InvoiceNo": invoice_numbers,
    "CustomerID": customer_ids,
    "StockCode": stock_codes,
    "Quantity": quantities,
    "UnitPrice": unit_prices,
    "InvoiceDate": invoice_dates
})

# Shuffle rows
online_retail = online_retail.sample(frac=1, random_state=42).reset_index(drop=True)

# Save as CSV
online_retail.to_csv("OnlineRetail.csv", index=False)

print("OnlineRetail.csv created successfully!")
print("\nFirst 5 rows:")
print(online_retail.head())