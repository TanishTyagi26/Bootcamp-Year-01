import pandas as pd
import numpy as np

# Make random values reproducible
np.random.seed(42)

# Create Patient IDs
patients = [f"P{str(i).zfill(3)}" for i in range(1, 21)]

rows = []

for patient in patients:

    # Random number of visits (8 to 15)
    visits = np.random.randint(8, 16)

    # Starting date
    start_date = pd.Timestamp("2024-01-01")

    # Random visit dates throughout the year
    visit_dates = start_date + pd.to_timedelta(
        np.sort(np.random.randint(0, 365, visits)),
        unit="D"
    )

    # Generate patient vitals
    systolic_bp = np.random.randint(110, 181, visits).astype(float)
    diastolic_bp = np.random.randint(70, 111, visits).astype(float)
    cholesterol = np.random.randint(150, 281, visits).astype(float)
    blood_sugar = np.random.randint(80, 221, visits).astype(float)

    # Add some missing values
    systolic_bp[np.random.choice(visits, 2, replace=False)] = np.nan
    cholesterol[np.random.choice(visits, 1)] = np.nan
    blood_sugar[np.random.choice(visits, 1)] = np.nan

    # Store records
    for i in range(visits):
        rows.append([
            patient,
            visit_dates[i],
            systolic_bp[i],
            diastolic_bp[i],
            cholesterol[i],
            blood_sugar[i]
        ])

# Create DataFrame
df = pd.DataFrame(rows, columns=[
    "PatientID",
    "VisitDate",
    "SystolicBP",
    "DiastolicBP",
    "Cholesterol",
    "BloodSugar"
])

# Save dataset
df.to_csv("ehr_dataset.csv", index=False)

print("Dataset generated successfully!")
print(df.head())