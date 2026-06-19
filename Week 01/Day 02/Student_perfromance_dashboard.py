#================= Student Performance Dashboard  ====================
#accept : student name , roll no., 5 subjects marks, attendance %age , Assignmnet score 
#cCalculate : Academic %age ,Attendance Status ,internal assessment Score , final performance score ,grade
#output : STUDENT PERFORMANCE DASHBOARD 
#    ==================================================== 
#   STudent Name :
#Roll .no :
#Subject 1 :
#Subject 2: etc
#
#Avg:
#GRade :
#/n
#Attendance:
#statues:
#/n
#performance index :
#/n
#/n
#result :
#pass/fail
#========================================================
#bonus features: scholarship eligibility , rank category , distinction certificate.

#================= Student Performance Dashboard ====================

print("STUDENT PERFORMANCE DASHBOARD")
print("====================================================")

student_name = input("Enter your name : ")
roll_no = int(input("Enter your Roll No. : "))
total_subj = int(input("Enter your total subjects : "))
attend_percent = float(input("Enter your attendance percentage : "))
assign_score = float(input("Enter your assignment score : "))

subj_name_list = []
subj_marks_list = []

# Subject Names
for i in range(total_subj):
    subj_name = input(f"Enter subject {i+1} name : ")
    subj_name_list.append(subj_name)
    print(f"{subj_name} entered successfully.....")

print()

# Subject Marks
for i in range(total_subj):
    subj_marks = float(input(f"Enter marks for {subj_name_list[i]} : "))
    subj_marks_list.append(subj_marks)
    print("Marks entered successfully.....")

# Academic Percentage
total_marks = sum(subj_marks_list)
avg = total_marks / total_subj

# Attendance Status
if attend_percent >= 75:
    attendance_status = "Good Attendance"
else:
    attendance_status = "Short Attendance"

# Internal Assessment Score
internal_assessment = (assign_score + attend_percent) / 2

# Final Performance Index
performance_index = (avg * 0.8) + (internal_assessment * 0.2)

# Grade
if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "F"

# Result
if min(subj_marks_list) >= 33:
    result = "PASS"
else:
    result = "FAIL"

# Scholarship Eligibility
if avg >= 90 and attend_percent >= 85:
    scholarship = "Eligible"
else:
    scholarship = "Not Eligible"

# Rank Category
if avg >= 90:
    rank_category = "Top Performer"
elif avg >= 75:
    rank_category = "Excellent"
elif avg >= 60:
    rank_category = "Good"
else:
    rank_category = "Average"

# Distinction Certificate
if avg >= 75:
    distinction = "Awarded"
else:
    distinction = "Not Awarded"

# ================= Dashboard =================

print("\n")
print("====================================================")
print("           STUDENT PERFORMANCE DASHBOARD")
print("====================================================")

print(f"Student Name : {student_name}")
print(f"Roll No. : {roll_no}")

print("\nSubjects and Marks")
for subject, marks in zip(subj_name_list, subj_marks_list):
    print(subject, ":", marks)

print("\nAverage Percentage :", round(avg, 2))
print(f"Grade : {grade}")

print("\nAttendance :", attend_percent, "%")
print(f"Status : {attendance_status}" )

print("\nInternal Assessment Score :", round(internal_assessment, 2))
print(f"Performance Index : {performance_index}" )

print(f"\nResult : {result}" )

print("\nScholarship Eligibility :", scholarship)
print(f"Rank Category : {rank_category}" )
print(f"Distinction Certificate : {distinction}")

print("====================================================")





















