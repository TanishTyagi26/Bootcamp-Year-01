#  ================================ Multi-Role Staff System  ================================ 

# Design: Person Employee (Teacher, AdminStaff) using hierarchical inheritance. Teacher adds subjects list and teach() method. AdminStaff adds designation and admin_task(). Use multiple inheritance to create a TeacherAdmin class combining both. Demonstrate MRO.

# (Hint: print(TeacherAdmin. _mro); in TeacherAdmin.init call super() and check cooperative MRO)


class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)


class Employee(Person):
    def __init__(self, emp_id, **kwargs):
        self.emp_id = emp_id
        super().__init__(**kwargs)


class Teacher(Employee):
    def __init__(self, subjects, **kwargs):
        self.subjects = subjects
        super().__init__(**kwargs)

    def teach(self):
        print(self.name, "is teaching", self.subjects)


class AdminStaff(Employee):
    def __init__(self, designation, **kwargs):
        self.designation = designation
        super().__init__(**kwargs)

    def admin_task(self):
        print(self.name, "is working as", self.designation)


class TeacherAdmin(Teacher, AdminStaff):
    def __init__(self, name, age, emp_id, subjects, designation):
        super().__init__(name=name,age=age,emp_id=emp_id,subjects=subjects,designation=designation)


ta = TeacherAdmin("Rahul",35,101,["Python", "AI"],"Vice Principal")

ta.teach()
ta.admin_task()

print("MRO:")
print(TeacherAdmin.__mro__)