# #               =================  Secure Student Record ======================

# Create a Student class with private__roll_no, __marks_list, and protected _grade. Add @property for gpa (computed as avg marks/10), a setter that validates marks are 0-100, and a classmethod count() tracking total students created.

#  (Hint: Use @property + @gpa.setter; validate in setter; use class variable for count)


class Student:
    _count=0
    def __init__(self,roll_no,marks_list,grade):
        self.__roll_no=roll_no
        self.__marks_list=[]
        self._grade=grade

        self.gpa=marks_list

        Student._count+=1

    @property
    def gpa(self):
        avg_marks=sum(self.__marks_list)/len(self.__marks_list)
        return avg_marks/10

    @gpa.setter
    def gpa(self,marks_list):
        for mark in marks_list:
            if mark<0 or mark>100:
                raise ValueError("Marks must be between 0 and 100")
            self.__marks_list=marks_list

    @classmethod
    def count(cls):
        return cls._count

# Creating student objects
stu1=Student(414,[98,99,100],"A")
stu2=Student(415,[50,45,38],"C")

# Display GPA
print(stu1.gpa)
print(stu2.gpa)

# Display total students created
print("Total Students:", Student.count())




