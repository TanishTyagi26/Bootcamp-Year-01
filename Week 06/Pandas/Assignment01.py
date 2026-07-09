import pandas as pd
import numpy as np

roll = range(1, 101)
names = [f"Student{i}" for i in range(1, 101)]

python_marks = np.random.randint(30, 101, 100)
java_marks = np.random.randint(30, 101, 100)
ml_marks = np.random.randint(30, 101, 100)
cloud_marks = np.random.randint(30, 101, 100)
attendance = np.random.randint(50, 101, 100)

df = pd.DataFrame({
    "Roll": roll,
    "Name": names,
    "Python": python_marks,
    "Java": java_marks,
    "ML": ml_marks,
    "Cloud": cloud_marks,
    "Attendance": attendance
})

df["Total"] = df["Python"] + df["Java"] + df["ML"] + df["Cloud"]

df["Percentage"] = (df["Total"] / 400) * 100

def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(grade)


df["Rank"] = df["Percentage"].rank(ascending=False, method="min").astype(int)

top10 = df.sort_values(by="Percentage", ascending=False).head(10)
low_marks = (
    (df["Python"] < 40).astype(int) +
    (df["Java"] < 40).astype(int) +
    (df["ML"] < 40).astype(int) +
    (df["Cloud"] < 40).astype(int)
)

below40 = df[low_marks >= 2]

topper = df.loc[df["Percentage"].idxmax()]

low_attendance = df[df["Attendance"] < 75]

top10.to_csv("Topper_List.csv", index=False)

print("\nComplete Student Data")
print(df)

print("\nTop 10 Students")
print(top10)

print("\nStudents below 40% in at least two subjects")
print(below40)

print("\nDepartment Topper")
print(topper)

print("\nAttendance below 75%")
print(low_attendance)

print("\nTopper list exported successfully as 'Topper_List.csv'")