# ===============================question 1===============================

#Global Climate Change & Thermal Anomaly Tracking
# Objective: Clean, resample, and analyze unstructured climate sensor data to detect regional warming patterns.
# Data Profile: A massive dataset with millions of rows containing hourly temperature readings, sensor IDs, latitudes, longitudes, and quality flags.

#==================== Student Tasks:===============================

# Pandas: Load chunks of the dataset using read_csv(chunksize=...). Handle missing or corrupted flags, convert timestamps, and set a MultiIndex on (Country, State, Timestamp).
# NumPy: Use np.where() and vectorization to replace flagged anomaly values with localized rolling medians.
# Matplotlib: Plot a dual-axis chart showing the global annual temperature anomaly trend alongside a sub-plot heatmap tracking the standard deviation of temperatures by latitude band over the decades.


# ===========================
# STEP 1 : Import Libraries
# ===========================
import os

print(os.getcwd())



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===========================
# STEP 2 : Read CSV in Chunks
# ===========================

chunk_size = 100000

chunks = pd.read_csv(
    "climate_data.csv",
    chunksize=chunk_size
)

# Empty list to store processed chunks
processed_chunks = []

# ===========================
# STEP 3 : Process Each Chunk
# ===========================

for chunk in chunks:

    # Convert Timestamp column into datetime format
    chunk["Timestamp"] = pd.to_datetime(chunk["Timestamp"])

    # Fill missing temperatures with median
    chunk["Temperature"] = chunk["Temperature"].fillna(
        chunk["Temperature"].median()
    )

    # Keep only rows having Good quality
    chunk = chunk[chunk["QualityFlag"].isin(["Good"])]

    # Store cleaned chunk
    processed_chunks.append(chunk)

# ===========================
# STEP 4 : Combine Chunks
# ===========================

df = pd.concat(
    processed_chunks,
    ignore_index=True
)

# ===========================
# STEP 5 : Create MultiIndex
# ===========================

df = df.set_index(
    ["Country", "State", "Timestamp"]
)

# ===========================
# STEP 6 : Rolling Median
# ===========================

rolling_median = (
    df["Temperature"]
    .rolling(window=5, center=True)
    .median()
)

# ===========================
# STEP 7 : Replace Anomalies
# ===========================

df["Temperature"] = np.where(
    df["Temperature"] == 999,
    rolling_median,
    df["Temperature"]
)

# ===========================
# STEP 8 : Extract Year
# ===========================

df["Year"] = (
    df.index
    .get_level_values("Timestamp")
    .year
)

# ===========================
# STEP 9 : Annual Temperature
# ===========================

annual_temp = (
    df.groupby("Year")["Temperature"]
    .mean()
)

# ===========================
# STEP 10 : Temperature Anomaly
# ===========================

baseline = annual_temp.mean()

temperature_anomaly = annual_temp - baseline

# ===========================
# STEP 11 : Reset Index
# ===========================

df = df.reset_index()

# ===========================
# STEP 12 : Latitude Bands
# ===========================

df["LatitudeBand"] = pd.cut(
    df["Latitude"],
    bins=np.arange(-90, 91, 10)
)

# ===========================
# STEP 13 : Decades
# ===========================

df["Decade"] = (
    df["Year"] // 10
) * 10

# ===========================
# STEP 14 : Standard Deviation
# ===========================

std_table = (
    df.groupby(
        ["LatitudeBand", "Decade"]
    )["Temperature"]
    .std()
    .unstack()
)

# ===========================
# STEP 15 : Create Figure
# ===========================

fig, (ax1, ax2) = plt.subplots(
    2,
    1,
    figsize=(12, 10)
)

# ===========================
# STEP 16 : Line Graph
# ===========================

ax1.plot(
    temperature_anomaly.index,
    temperature_anomaly.values,
    color="red",
    marker="o"
)

ax1.set_title(
    "Global Annual Temperature Anomaly"
)

ax1.set_xlabel("Year")

ax1.set_ylabel(
    "Temperature Anomaly"
)

ax1.grid(True)

# ===========================
# STEP 17 : Heatmap
# ===========================

heatmap = ax2.imshow(
    std_table,
    aspect="auto",
    cmap="coolwarm",
    origin="lower"
)

ax2.set_title(
    "Temperature Standard Deviation by Latitude Band"
)

ax2.set_xlabel("Decade")

ax2.set_ylabel("Latitude Band")

ax2.set_xticks(
    range(len(std_table.columns))
)

ax2.set_xticklabels(
    std_table.columns
)

ax2.set_yticks(
    range(len(std_table.index))
)

ax2.set_yticklabels(
    std_table.index.astype(str)
)

plt.colorbar(
    heatmap,
    ax=ax2
)

# ===========================
# STEP 18 : Display Graph
# ===========================

plt.tight_layout()

plt.show() 



































































