# Task: Employee objects with default constructor values

# Create an Employee class using default parameter values for optional fields

# Create a class Employee with _init_(self, name, department="General", bonus=0). Add a method annual_summary() that prints the employee's name, department, and total pay (assume a fixed base salary of 30000 plus bonus). Create employees using all three calling styles: full arguments, partial arguments, and only the required name.


class Employee:
    def __init__(self,name,department="General",bonus=0):
        self.name=name
        self.department=department
        self.bonus=bonus


    def annual_summary(self):
        print(f"Name : {self.name}\nDepartment : {self.department}\nTotal Pay : {30000+self.bonus}\n ")

emp1=Employee("Tanish","TECH",20000)
emp2=Employee("Ayush","AI",)
emp3=Employee("Anik")

emp1.annual_summary()
emp2.annual_summary()
emp3.annual_summary()
