#================= student Performance Analyzer  ==================

def student_report(name,marks):
    print("-------------------- STUDENT REPORT ----------------------")
    print(f"Name : {name}")
    print(f"Marks: {marks}")
    print("----------------------------------------------------------")
    print()

def add_bonus(marks):
    print(f"Inside Function Marks : {marks+5}")
    print(f"Outside Function Marks : {marks}")
    print()

def sum_marks(n):
    if n==0:
        return 0
    else:
        return n+sum_marks(n-1)

def apply_operation(function,value):
    if function==1 :
        def square (value):
            return value*value
        return square(value)
    
    elif function==2 :
        def cube(value):
            return value*value*value
        return cube(value)
    
    else :
        print("Invalid Input ...")


#---Main Program---
name=str(input("Enter Your Name : "))
marks=int(input("enter your Marks : "))
student_report(name,marks)
add_bonus(marks)

n=int(input("enter a number for recursive sum : "))
Recursive_sum=sum_marks(n)
print("Recursive Sum = " , Recursive_sum)
print()

print("Choose Operation : ")
print("1. Square ")
print("2. Cube")

choice=int(input("Enter Choice : "))
number =int(input("enter Number : "))
print()
print("Result = ", apply_operation(choice,number))
