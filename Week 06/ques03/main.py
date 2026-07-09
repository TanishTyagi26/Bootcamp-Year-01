# E-Commerce Customer Lifetime Value (CLV) & Cohort Analysis

# Objective: Segment customers into behavioral cohorts based on their first purchase month and track retention.

# Data Profile: Raw transactional data containing InvoiceNo, CustomerID, StockCode, Quantity, UnitPrice, and InvoiceDate.

# Student Tasks:

# Pandas: Parse dates and extract the cohort month. Use groupby and transform to assign each customer to a cohort. Pivot the data to create a retention matrix showing the percentage of active customers over a 12-month period.NumPy: Calculate matrix-wide percentage decays and compute the rolling 30-day cumulative spend per customer using np.cumsum().

# Matplotlib: Draw a highly polished seaborn-style heatmap of the cohort retention matrix, complete with percentage annotations, custom color gradients (cmap='YIGnBu'), and explicit axis labels.




# ============================================================
# E-Commerce Customer Lifetime Value (CLV) & Cohort Analysis
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
plt.style.use("seaborn-v0_8")

df = pd.read_csv("OnlineRetail.csv", encoding="ISO-8859-1")

# -----------------------------
# Data Cleaning
# -----------------------------
df = df.dropna(subset=['CustomerID'])

df['CustomerID'] = df['CustomerID'].astype(int)

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Remove cancelled invoices
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Remove negative quantities
df = df[df['Quantity'] > 0]

# Calculate Sales
df['Sales'] = df['Quantity'] * df['UnitPrice']

# -----------------------------
# Create Cohort Month
# -----------------------------
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')

df['CohortMonth'] = (
    df.groupby('CustomerID')['InvoiceMonth']
      .transform('min')
)

# -----------------------------
# Calculate Cohort Index
# -----------------------------
invoice_year = df['InvoiceMonth'].dt.year
invoice_month = df['InvoiceMonth'].dt.month

cohort_year = df['CohortMonth'].dt.year
cohort_month = df['CohortMonth'].dt.month

df['CohortIndex'] = (
    (invoice_year - cohort_year) * 12 +
    (invoice_month - cohort_month) + 1
)

# -----------------------------
# Cohort Analysis
# -----------------------------
cohort_data = (
    df.groupby(['CohortMonth', 'CohortIndex'])['CustomerID']
      .nunique()
      .reset_index()
)

cohort_matrix = cohort_data.pivot(
    index='CohortMonth',
    columns='CohortIndex',
    values='CustomerID'
)

# -----------------------------
# Retention Matrix
# -----------------------------
cohort_size = cohort_matrix.iloc[:, 0]

retention = cohort_matrix.divide(cohort_size, axis=0)

# First 12 months only
retention = retention.iloc[:, :12]

retention_percent = retention * 100

print("\nCustomer Retention Matrix (%)")
print(retention_percent.round(2))

# ============================================================
# NumPy Task 1
# Matrix-wide Percentage Decay
# ============================================================

retention_array = retention.fillna(0).to_numpy()

decay = np.diff(retention_array, axis=1)

print("\nMonthly Percentage Decay")
print(decay)

print("\nAverage Monthly Decay:")
print(np.mean(decay))

# ============================================================
# NumPy Task 2
# Rolling 30-Day Cumulative Spend
# ============================================================

df = df.sort_values(['CustomerID', 'InvoiceDate'])

daily_spend = (
    df.groupby(['CustomerID', 'InvoiceDate'])['Sales']
      .sum()
      .reset_index()
)

# Cumulative Spend using np.cumsum()
daily_spend['CumulativeSpend'] = (
    daily_spend.groupby('CustomerID')['Sales']
               .transform(lambda x: np.cumsum(x))
)

# Rolling 30-Day Spend
daily_spend = daily_spend.set_index('InvoiceDate')

daily_spend['Rolling30DaySpend'] = (
    daily_spend.groupby('CustomerID')['Sales']
               .rolling('30D')
               .sum()
               .reset_index(level=0, drop=True)
)

daily_spend = daily_spend.reset_index()

print("\nRolling 30-Day Spend")
print(daily_spend.head())

# ============================================================
# Customer Lifetime Value (CLV)
# ============================================================

clv = (
    df.groupby('CustomerID')['Sales']
      .sum()
      .sort_values(ascending=False)
)

print("\nTop 10 Customers by CLV")
print(clv.head(10))

# ============================================================
# Cohort Retention Heatmap
# ============================================================

fig, ax = plt.subplots(figsize=(14, 8))

heatmap = ax.imshow(
    retention_percent,
    cmap='YlGnBu',
    aspect='auto',
    interpolation='nearest'
)

# Axis labels
ax.set_title(
    "Customer Cohort Retention Matrix",
    fontsize=18,
    fontweight='bold'
)

ax.set_xlabel("Months Since First Purchase", fontsize=13)
ax.set_ylabel("Cohort Month", fontsize=13)

# Tick labels
ax.set_xticks(np.arange(retention_percent.shape[1]))
ax.set_xticklabels(retention_percent.columns)

ax.set_yticks(np.arange(retention_percent.shape[0]))
ax.set_yticklabels(retention_percent.index.astype(str))

# Annotate percentages
for i in range(retention_percent.shape[0]):
    for j in range(retention_percent.shape[1]):
        value = retention_percent.iloc[i, j]

        if not np.isnan(value):
            ax.text(
                j,
                i,
                f"{value:.0f}%",
                ha='center',
                va='center',
                color='black',
                fontsize=8
            )

# Color bar
cbar = plt.colorbar(heatmap)
cbar.set_label("Retention (%)")

plt.tight_layout()
plt.show()










