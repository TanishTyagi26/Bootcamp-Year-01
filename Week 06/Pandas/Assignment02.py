import pandas as pd
import numpy as np

# Create Data
departments = ["IT", "HR", "Finance", "Marketing", "Sales"]

df = pd.DataFrame({
    "EmpID": range(1, 501),
    "Department": np.random.choice(departments, 500),
    "Experience": np.random.randint(1, 31, 500),
    "Salary": np.random.randint(25000, 120001, 500),
    "Performance": np.random.randint(1, 6, 500)
})

# 1. Save as CSV
df.to_csv("Employees.csv", index=False)

# 2. Save as Excel
df.to_excel("Employees.xlsx", index=False)

# 3. Read both files
csv_data = pd.read_csv("Employees.csv")
excel_data = pd.read_excel("Employees.xlsx")

# 4. Verify both are identical
print("Files are identical:", csv_data.equals(excel_data))

# 5. Average salary department-wise
print("\nAverage Salary Department-wise")
print(df.groupby("Department")["Salary"].mean())

# 6. Highest performer
highest_performer = df[df["Performance"] == df["Performance"].max()]
print("\nHighest Performer")
print(highest_performer)

# 7. Salary greater than department average
dept_avg = df.groupby("Department")["Salary"].transform("mean")
high_salary = df[df["Salary"] > dept_avg]
print("\nEmployees with Salary Above Department Average")
print(high_salary)

# 8. Experience >15 and Performance <3
experienced = df[(df["Experience"] > 15) & (df["Performance"] < 3)]
print("\nExperienced Employees with Low Performance")
print(experienced)

# 9. Bonus Column
df["Bonus"] = np.where(
    df["Performance"] >= 4,
    df["Salary"] * 0.10,
    df["Salary"] * 0.05
)

# 10. Export Bonus >10000
bonus_emp = df[df["Bonus"] > 10000]
bonus_emp.to_csv("Bonus_Employees.csv", index=False)

print("\nEmployees with Bonus Above ₹10,000 exported successfully.")

