#wap to check student's performance using nested (if -else- elif):
#conditions :marks>=40(pass/fail)-----if pass check for distinction (marks>=90),first division(marks>=75),second division(marks>=60), else third division
def perfomance(marks):
    if marks >=40:
        if marks>=90:
            print(f"Congratulations you got Distinction ")
        elif marks>=75:
            print("first division")
        elif marks>=60:
            print("Second division")
        else:
            print("Third Division")
    else:
        print("Sorry , but you failed the examination")
while True:
    marks=float (input("enter your marks :"))
    perfomance(marks)






