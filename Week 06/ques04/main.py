import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, atan2

# Read dataset
df = pd.read_csv("taxi_gps.csv")

# Convert Timestamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Get previous GPS coordinates
df["PrevLat"] = df["Latitude"].shift()
df["PrevLon"] = df["Longitude"].shift()

# Function to calculate Haversine distance
def haversine(lat1, lon1, lat2, lon2):
    if pd.isna(lat1):
        return 0

    R = 6371  # Earth's radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)

    a = sin(dLat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dLon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

# Calculate distance between consecutive GPS points
df["Distance"] = df.apply(
    lambda row: haversine(
        row["PrevLat"],
        row["PrevLon"],
        row["Latitude"],
        row["Longitude"]
    ),
    axis=1
)

# Create location grids
df["GridLat"] = df["Latitude"].round(2)
df["GridLon"] = df["Longitude"].round(2)

# Average speed in each grid
traffic = df.groupby(["GridLat", "GridLon"])["Speed"].mean()

# Speed categories
bins = [20, 40]
states = ["Gridlock", "Slow", "Free Flow"]

df["TrafficState"] = np.digitize(df["Speed"], bins)
df["TrafficState"] = df["TrafficState"].map(lambda x: states[x])

# Acceleration
df["Acceleration"] = np.append(np.diff(df["Speed"]), 0)

# Scatter plot
plt.figure(figsize=(8,6))
plt.scatter(
    df["Longitude"],
    df["Latitude"],
    c=df["Speed"],
    cmap="RdYlGn"
)
plt.colorbar(label="Speed (km/h)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Traffic Congestion Map")
plt.show()

# Day of week
df["Day"] = df["Timestamp"].dt.day_name()

# Average speed per day
weekly = df.groupby("Day")["Speed"].mean()

# Radar chart
labels = weekly.index
values = weekly.values

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

values = np.concatenate((values, [values[0]]))
angles = np.concatenate((angles, [angles[0]]))

plt.figure(figsize=(7,7))
ax = plt.subplot(111, polar=True)

ax.plot(angles, values)
ax.fill(angles, values, alpha=0.3)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.title("Average Traffic Speed by Day")
plt.show()