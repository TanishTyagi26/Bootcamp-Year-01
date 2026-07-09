import numpy as np

patients = np.random.randint(50, 251, size=(30, 5))

print("Patient Data:\n")
print(patients)
mean = np.mean(patients, axis=0)
print("\nDepartment-wise Mean:")
print(mean)
median = np.median(patients, axis=0)
print("\nDepartment-wise Median:")
print(median)
std = np.std(patients, axis=0)
print("\nDepartment-wise Standard Deviation:")
print(std)
highest = np.max(patients, axis=0)
print("\nHighest Patient Count:")
print(highest)
lowest = np.min(patients, axis=0)
print("\nLowest Patient Count:")
print(lowest)
upper = mean + 2 * std
lower = mean - 2 * std
outliers = (patients < lower) | (patients > upper)
print("\nOutlier Locations (True = Outlier):")
print(outliers)
new_patients = patients.copy()

for i in range(30):
    for j in range(5):
        if patients[i][j] < lower[j] or patients[i][j] > upper[j]:
            new_patients[i][j] = mean[j]

print("\nData After Replacing Outliers:")
print(new_patients)