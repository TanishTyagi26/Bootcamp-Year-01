# ___________________________________student management system ___________________________________



def remaining_courses(completed_courses):
    courses_done =  40-completed_courses 
    course_completion_percentage = (courses_done/40)*100
    return courses_done ,course_completion_percentage 

student_name = str(input("enter your name :"))
roll_no = int(input("enter your Roll No. :"))
age = int(input("enter your age :"))
Program =str(input("enter your program :"))
cgpa = float(input("enter your cgpa :"))
completed_courses = int(input("enter number of completed courses :"))
print("============Student Report=========")
print(f"Name : {student_name}")
print(f"Roll.No.: {roll_no}")
print(f"Age : {age}")
print(f"Program : {Program}")
print(f"CGPA : {cgpa}")
print(f"Completed courses : {completed_courses}")
remaining_courses , course_percentage = remaining_courses(completed_courses)
print(f"Remaining Courses : {remaining_courses}")
print(f"Degree Completion : {course_percentage} ")
print("==========================================")
