import pandas as pd
import random
from datetime import datetime, timedelta

# Empty list to store data
data = []

# Starting date and time
start_time = datetime(2026, 7, 1, 6, 0, 0)

# Make random values repeatable
random.seed(42)

# Generate data for 10 taxis
for vehicle in range(1, 11):

    # Random starting location (around Delhi)
    latitude = 28.6139 + random.uniform(-0.03, 0.03)
    longitude = 77.2090 + random.uniform(-0.03, 0.03)

    current_time = start_time

    # Generate 50 GPS pings for each taxi
    for i in range(50):

        # Slight movement in GPS location
        latitude += random.uniform(-0.0015, 0.0015)
        longitude += random.uniform(-0.0015, 0.0015)

        # Random speed between 5 and 70 km/h
        speed = random.randint(5, 70) + random.uniform(-3, 3)

        # Keep speed within 0–80 km/h
        speed = max(0, min(speed, 80))

        # Add one record
        data.append([
            f"V{vehicle:03d}",
            current_time.strftime("%Y-%m-%d %H:%M:%S"),
            round(latitude, 6),
            round(longitude, 6),
            round(speed, 2)
        ])

        # Next GPS ping after 2 minutes
        current_time += timedelta(minutes=2)

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "VehicleID",
    "Timestamp",
    "Latitude",
    "Longitude",
    "Speed"
])

# Save as CSV
df.to_csv("taxi_gps.csv", index=False)

# Save as Excel
df.to_excel("taxi_gps.xlsx", index=False)

# Display first 10 rows
print(df.head(10))

# Display total records
print("\nTotal Records:", len(df))