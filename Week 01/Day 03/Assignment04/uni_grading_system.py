#wap for university having percentage based grading system ,cgpa
#conditions : 90-100->A+ //80-89->A // 70-79->B+ //60-69 -> B// 50-59->C // <50->F_______________////-----grade points :10,9,8,7,6,4,0 ___________letter grades A+,A,B+,B,C+,C,D,F


def grading_system(marks):
    percentage=marks/100
    if percentage>=90 :
        grade,remark ,gpa = "O","Outstanding",10
    elif percentage>=80 :
        grade,remark ,gpa = "A+","Excellent",9
    elif percentage >=70 :
        grade,remark ,gpa = "A","Best",8
    elif percentage >=60 :
        grade,remark ,gpa = "B+","Better",7
    elif percentage >=50 :
        grade,remark ,gpa = "B","Good",6
    elif percentage >=40 :
        grade,remark ,gpa = "C","Keep it up !",5
    elif percentage>20 :
        grade,remark ,gpa = "D","Try Harder next time",4
    else:
        grade,remark ,gpa = "F","Fail",0

    print(f"grade : {grade} gpa : {gpa} remarks :{remark}")
    return grade,gpa,remark

while True:
    marks=float(input('enter your total marks : '))

    result=grading_system(marks)
    print(result)
