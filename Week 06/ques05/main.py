# ============================================================
# TELECOMMUNICATIONS CUSTOMER CHURN ANALYSIS
# EDA + FEATURE ENGINEERING
# ============================================================

# ----------------------------
# Import Libraries
# ----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Generate Dataset
# ----------------------------
np.random.seed(42)

n = 1000

gender = np.random.choice(["Male", "Female"], n)

senior = np.random.choice(
    ["Yes", "No"],
    n,
    p=[0.2, 0.8]
)

tenure = np.random.randint(1, 73, n)

monthly_charges = np.random.randint(20, 121, n)

total_charges = (
    tenure * monthly_charges
    + np.random.randint(-100, 100, n)
)

contract = np.random.choice(
    ["Month-to-month", "One Year", "Two Year"],
    n,
    p=[0.5, 0.3, 0.2]
)

internet = np.random.choice(
    ["Fiber", "DSL", "None"],
    n,
    p=[0.5, 0.4, 0.1]
)

churn = np.random.choice(
    ["Yes", "No"],
    n,
    p=[0.3, 0.7]
)

# Store TotalCharges as string intentionally
total_charges = total_charges.astype(str)

# Add some invalid values intentionally
for i in np.random.choice(n, 15, replace=False):
    total_charges[i] = "Unknown"

# Create DataFrame
df = pd.DataFrame({
    "Gender": gender,
    "SeniorCitizen": senior,
    "Tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "ContractType": contract,
    "InternetService": internet,
    "Churn": churn
})

# Save Dataset
df.to_csv("telecom_churn.csv", index=False)

print("=" * 60)
print("Dataset Generated Successfully!")
print("=" * 60)

# -------------------------------------------------
# Read Dataset
# -------------------------------------------------

df = pd.read_csv("telecom_churn.csv")

print("\nFirst Five Records\n")
print(df.head())

print("\nDataset Information\n")
print(df.info())

# -------------------------------------------------
# Fix Data Type Mismatch
# -------------------------------------------------

print("\nConverting TotalCharges into Numeric...")

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# -------------------------------------------------
# Handle Missing Values
# -------------------------------------------------

print("\nMissing Values\n")
print(df.isnull().sum())

df["TotalCharges"].fillna(
    df["TotalCharges"].median(),
    inplace=True
)

print("\nMissing Values After Filling\n")
print(df.isnull().sum())

# -------------------------------------------------
# One Hot Encoding
# -------------------------------------------------

print("\nApplying One Hot Encoding...\n")

df = pd.get_dummies(
    df,
    columns=[
        "Gender",
        "SeniorCitizen",
        "ContractType",
        "InternetService"
    ],
    drop_first=True
)

# -------------------------------------------------
# Discretize Tenure
# -------------------------------------------------

df["TenureGroup"] = pd.qcut(
    df["Tenure"],
    q=4,
    labels=[
        "Q1",
        "Q2",
        "Q3",
        "Q4"
    ]
)

print("\nTenure Groups Created Successfully.\n")

# -------------------------------------------------
# Detect Outliers Using NumPy Percentile
# -------------------------------------------------

print("=" * 60)
print("OUTLIER DETECTION")
print("=" * 60)

Q1 = np.percentile(
    df["TotalCharges"],
    25
)

Q3 = np.percentile(
    df["TotalCharges"],
    75
)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)

upper_limit = Q3 + (1.5 * IQR)

outliers = df[
    (df["TotalCharges"] < lower_limit) |
    (df["TotalCharges"] > upper_limit)
]

print("Q1 :", Q1)
print("Q3 :", Q3)
print("IQR :", IQR)
print("Lower Limit :", lower_limit)
print("Upper Limit :", upper_limit)
print("Number of Outliers :", len(outliers))

# -------------------------------------------------
# Create Original Dataset Again for Visualization
# -------------------------------------------------

original_df = pd.read_csv("telecom_churn.csv")

original_df["TotalCharges"] = pd.to_numeric(
    original_df["TotalCharges"],
    errors="coerce"
)

original_df["TotalCharges"].fillna(
    original_df["TotalCharges"].median(),
    inplace=True
)

churn_yes = original_df[
    original_df["Churn"] == "Yes"
]

churn_no = original_df[
    original_df["Churn"] == "No"
]

# -------------------------------------------------
# Visualization
# -------------------------------------------------

fig, axes = plt.subplots(
    3,
    3,
    figsize=(16, 12)
)

# ---------------- Row 1 Histograms ----------------

axes[0, 0].hist(
    churn_yes["Tenure"],
    bins=15,
    alpha=0.6,
    label="Churn"
)

axes[0, 0].hist(
    churn_no["Tenure"],
    bins=15,
    alpha=0.6,
    label="Retained"
)

axes[0, 0].set_title("Tenure Distribution")
axes[0, 0].legend()

axes[0, 1].hist(
    churn_yes["MonthlyCharges"],
    bins=15,
    alpha=0.6,
    label="Churn"
)

axes[0, 1].hist(
    churn_no["MonthlyCharges"],
    bins=15,
    alpha=0.6,
    label="Retained"
)

axes[0, 1].set_title("Monthly Charges")
axes[0, 1].legend()

axes[0, 2].hist(
    churn_yes["TotalCharges"],
    bins=15,
    alpha=0.6,
    label="Churn"
)

axes[0, 2].hist(
    churn_no["TotalCharges"],
    bins=15,
    alpha=0.6,
    label="Retained"
)

axes[0, 2].set_title("Total Charges")
axes[0, 2].legend()

# ---------------- Row 2 Boxplots ----------------

axes[1, 0].boxplot(
    [
        churn_yes["Tenure"],
        churn_no["Tenure"]
    ],
    tick_labels=[
        "Churn",
        "Retained"
    ]
)

axes[1, 0].set_title("Tenure Boxplot")

axes[1, 1].boxplot(
    [
        churn_yes["MonthlyCharges"],
        churn_no["MonthlyCharges"]
    ],
    tick_labels=[
        "Churn",
        "Retained"
    ]
)

axes[1, 1].set_title("Monthly Charges Boxplot")

axes[1, 2].boxplot(
    [
        churn_yes["TotalCharges"],
        churn_no["TotalCharges"]
    ],
    tick_labels=[
        "Churn",
        "Retained"
    ]
)

axes[1, 2].set_title("Total Charges Boxplot")

# ---------------- Row 3 Histograms ----------------

axes[2, 0].hist(
    churn_yes["Tenure"],
    bins=20,
    alpha=0.6,
    label="Churn"
)

axes[2, 0].hist(
    churn_no["Tenure"],
    bins=20,
    alpha=0.6,
    label="Retained"
)

axes[2, 0].set_title("Tenure Comparison")
axes[2, 0].legend()

axes[2, 1].hist(
    churn_yes["MonthlyCharges"],
    bins=20,
    alpha=0.6,
    label="Churn"
)

axes[2, 1].hist(
    churn_no["MonthlyCharges"],
    bins=20,
    alpha=0.6,
    label="Retained"
)

axes[2, 1].set_title("Monthly Charges Comparison")
axes[2, 1].legend()

axes[2, 2].hist(
    churn_yes["TotalCharges"],
    bins=20,
    alpha=0.6,
    label="Churn"
)

axes[2, 2].hist(
    churn_no["TotalCharges"],
    bins=20,
    alpha=0.6,
    label="Retained"
)

axes[2, 2].set_title("Total Charges Comparison")
axes[2, 2].legend()

plt.tight_layout()
plt.show()

# -------------------------------------------------
# Feature Matrix
# -------------------------------------------------

print("\nPreparing Feature Matrix...\n")

X = df.drop(
    columns=[
        "Churn"
    ]
)

y = df["Churn"]

print("=" * 60)
print("Feature Matrix (X)")
print("=" * 60)

print(X.head())

print("\nShape :", X.shape)

print("\n")

print("=" * 60)
print("Target Variable (y)")
print("=" * 60)

print(y.head())

print("\nShape :", y.shape)

print("\n")

print("=" * 60)
print("Feature Engineering Completed Successfully!")
print("=" * 60)