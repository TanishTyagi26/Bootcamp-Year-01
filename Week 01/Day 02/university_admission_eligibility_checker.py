#================= University  Admission eligibility checker  ====================
#accept : student name , age , class 12th % , entrance exam  score , category  
#check : eligibility ,scholarship status ,admission grade
#output : generate complete report 
#bonus features : input validation , type checking ,exception handling , %age calculations ,scholarship rules ,formatted report generation 





student_name = str (input("enter your name :"))
age = int (input("enter your Age :"))
percentage_12th = float(input("enter your class 12th percentage : "))
entrance_score = float(input("enter your entrance exam score :"))
category = str(input("enter your category  : "))

if percentage_12th and entrance_score >=50 :
    print(f"congratulations {student_name} you're eligible for admission")
else :
    print(f"we're sorry {student_name} but don't meet our criterias")

if percentage_12th and entrance_score >=90 :
    print(f"congratulations {student_name} you're eligible for Scholarship ")
else :
    print(f"we're sorry {student_name} but don't meet our criterias")










