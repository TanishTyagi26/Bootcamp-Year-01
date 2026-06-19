#__________________________ Lambda with Sorted()_________________________
#given a list of dict. containing students with keys'name' and 'gpa'.
#write a Lambda fn .to sort the list by GPA in Descending Order..
#print the Top 3 Students...

students = []

n = int(input("Enter number of students: "))

for i in range(n):
        name = input("Enter Name: ")
        gpa = float(input("Enter GPA: "))

        students.append({"name": name, "gpa": gpa})

sorted_students = sorted(
        students,
        key=lambda student: student["gpa"],
        reverse=True
)

print("Top 3 Students:")

for student in sorted_students[:3]:
        print(student["name"], "-", student["gpa"])
