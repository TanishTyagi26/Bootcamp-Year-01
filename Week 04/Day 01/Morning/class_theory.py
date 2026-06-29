# ================================  Metrhod Resolution Order =============================================

# M.R.O : python solves method call from left to right ,depth first using C3 lineraisation.

class A:
    def greet(self):return "Hello from A"

class B(A):
    def greet(self):return "Hello from B"

class C(A):
    def greet(self):return "Hello from C"

class D(B,C):                               # B is in left so B's greet will print 
    pass

d=D()
print(d.greet())
print(D.__mro__)    # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)



# ================================  isinstance() and issubclass() =============================================


class Vehicle:
    pass

class Car(Vehicle):
    pass

class ElectricCar(Car):
    pass

tesla=ElectricCar()



# isinstance() checks the object's class and its parents

print(isinstance(tesla,ElectricCar))    # True
print(isinstance(tesla,Car))            # True  <-- Inherits !
print(isinstance(tesla,Vehicle))        # True  <-- Inherits !
print(isinstance(tesla,str))            # False


# issubclass() checks the class hierarchy

print(issubclass(ElectricCar,Car))          # True
print(issubclass(ElectricCar,Vehicle))      # True
print(issubclass(Car,ElectricCar))          # False 




# ================================  Super() =============================================

# we can inherit using super()
# we can inherit attributes using => super().__init__(attr1,attr2,....)
# we can inherit methods using  =>  super().method_name()


class Person:
    def __init__(self,name,age):
        self.name,self.age=name,age

    def introduce(self):
        return f"Hi ! I'm {self.name},age {self.age}"


class Employee(Person):
    def __init__(self, name, age,emp_id,dept):
        super().__init__(name, age)                 # Extends --> dont repeat!
        # we can inherit attributes using => super().__init__(attr1,attr2,....)  here it's super().__init__(name, age) 

        self.emp_id=emp_id
        self.dept=dept

    def introduce(self):                   # Extends Parent Method
        base= super().introduce()          # Reuse Parent Result    
        # we can inherit methods using  =>  super().method_name()  here  it's super().introduce()

        return f"{base} ,ID = {self.emp_id}, Dept = {self.dept}"


class Manager(Employee):
    def __init__(self, name, age, emp_id, dept,team_size):
        super().__init__(name, age, emp_id, dept)
        self.team_size=team_size

    def introduce(self):
        return super().introduce() + f",Team={self.team_size}"


mngr=Manager("Dr. Farooq",38,"M001","CSE",12)
print(mngr.introduce())



# ================================  Abstract  Method and Abstract Class=============================================
# ABC =Abstract Base Class   => we cannot instantiate it directly this abstract class will have abstarct methods which are nothing but just simpole methods just they have @abstarctmethod at start
#NoTE : always remember abstract methods defined in abstract class  must be used in child class
# abc is the lib and ABC is a class in abc lib.

from abc import ABC , abstractmethod

class Shape(ABC):                       # Cannot instantiate directly!
    def __init__(self,color):
        self.color=color


    @abstractmethod                     # Must be overridden in child
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):                     # concrete method  -- inheritable
        return f"{self.color} : area = {self.area():.2f}"


class Circle(Shape):
    def __init__(self,r, color="blue"):
        super().__init__(color)
        self.r=r

    def area(self): return 3.14159 * self.r ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.r 

#Shape()                             # TypeError : cann't instantiate Abstract class
c=Circle(7)
print(c.describe())             # blue : area = 153.94































































































































































































































































































































































































































































































































































































