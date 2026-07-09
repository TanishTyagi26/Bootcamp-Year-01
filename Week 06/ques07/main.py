import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Generate Sample EHR Dataset
# -----------------------------

np.random.seed(42)

patients = [f"P{str(i).zfill(3)}" for i in range(1, 21)]

rows = []

for patient in patients:

    visits = np.random.randint(8, 16)

    start_date = pd.Timestamp("2024-01-01")

    visit_dates = start_date + pd.to_timedelta(
        np.sort(np.random.randint(0, 365, visits)),
        unit="D"
    )

    systolic = np.random.randint(110, 180, visits).astype(float)
    diastolic = np.random.randint(70, 110, visits).astype(float)
    cholesterol = np.random.randint(150, 280, visits).astype(float)
    sugar = np.random.randint(80, 220, visits).astype(float)

    # Introduce Missing Values
    systolic[np.random.choice(visits, 2, replace=False)] = np.nan
    cholesterol[np.random.choice(visits, 1)] = np.nan
    sugar[np.random.choice(visits, 1)] = np.nan

    for i in range(visits):

        rows.append([
            patient,
            visit_dates[i],
            systolic[i],
            diastolic[i],
            cholesterol[i],
            sugar[i]
        ])

df = pd.DataFrame(
    rows,
    columns=[
        "PatientID",
        "VisitDate",
        "SystolicBP",
        "DiastolicBP",
        "Cholesterol",
        "BloodSugar"
    ]
)

df.to_csv("ehr_dataset.csv", index=False)

print("\nDataset Preview\n")
print(df.head())

# -----------------------------
# Read Dataset
# -----------------------------

df = pd.read_csv("ehr_dataset.csv")

df["VisitDate"] = pd.to_datetime(df["VisitDate"])

# Sort by Patient and Date
df = df.sort_values(["PatientID", "VisitDate"])

# -----------------------------
# Handle Missing Values
# -----------------------------

columns = [
    "SystolicBP",
    "DiastolicBP",
    "Cholesterol",
    "BloodSugar"
]

df[columns] = (
    df.groupby("PatientID")[columns]
      .ffill(limit=2)
)

print("\nDataset After Forward Fill\n")
print(df.head())

# -----------------------------
# Aggregate Historical Statistics
# -----------------------------

summary = df.groupby("PatientID").agg({

    "SystolicBP": ["min", "max", "mean", "std"],

    "DiastolicBP": ["min", "max", "mean", "std"],

    "Cholesterol": ["min", "max", "mean", "std"],

    "BloodSugar": ["min", "max", "mean", "std"]

})

print("\nHistorical Statistics\n")
print(summary)

# -----------------------------
# Blood Pressure Trend using NumPy
# -----------------------------

slopes = []

for patient, group in df.groupby("PatientID"):

    group = group.dropna(subset=["SystolicBP"])

    if len(group) > 1:

        x = (
            group["VisitDate"] -
            group["VisitDate"].min()
        ).dt.days

        y = group["SystolicBP"]

        slope = np.polyfit(x, y, 1)[0]

    else:

        slope = np.nan

    slopes.append([patient, slope])

trend = pd.DataFrame(
    slopes,
    columns=["PatientID", "Slope"]
)

print("\nBlood Pressure Trend\n")
print(trend)

# -----------------------------
# High Risk Patients
# -----------------------------

high_risk = trend.sort_values(
    by="Slope",
    ascending=False
).head(3)

print("\nTop 3 High Risk Patients\n")
print(high_risk)

# -----------------------------
# Multi Panel Plot
# -----------------------------

fig, axes = plt.subplots(
    len(high_risk),
    1,
    figsize=(12, 10)
)

if len(high_risk) == 1:
    axes = [axes]

for ax, patient in zip(axes, high_risk["PatientID"]):

    patient_data = df[df["PatientID"] == patient]

    ax.plot(
        patient_data["VisitDate"],
        patient_data["SystolicBP"],
        marker="o",
        label="Systolic BP"
    )

    ax.plot(
        patient_data["VisitDate"],
        patient_data["DiastolicBP"],
        marker="s",
        label="Diastolic BP"
    )

    # High BP Zone
    ax.axhspan(
        140,
        200,
        color="red",
        alpha=0.2,
        label="High BP Zone"
    )

    # Normal Zone
    ax.axhspan(
        0,
        90,
        color="green",
        alpha=0.2,
        label="Normal Zone"
    )

    ax.set_title(f"Patient {patient}")

    ax.set_ylabel("Blood Pressure")

    ax.legend()

plt.xlabel("Visit Date")

plt.tight_layout()

plt.show()