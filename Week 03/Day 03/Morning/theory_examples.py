
#               ==============  Getters and Setters======================


# class BankAccount:
#     def __init__(self,owner,balance=0):
#         self.owner = owner          #public
#         self._bank="KRM Bank"       #protected
#         self.__balance=balance      #private

#         #Getter
#     def get_balance(self):
#             return self.__balance

#         #Setter with validation
#     def deposit(self,amount):
#             if amount<=0:
#                 raise ValueError ("Deposit must be Positive...")
#             self.__balance+=amount
#             print(f"Deposited Amount is : {amount}\nBalance Amount is : {self.__balance}")

#     def withdraw(self,amount):
#             if amount>self.__balance:
#                 raise ValueError("Insufficient Balance")
#             self.__balance-=amount

# #_________  object creation  ___________

# acc=BankAccount("Tanish",10000)
# acc.deposit(500)
# print(acc.get_balance())
# # acc.__balance()        # AttributeError => bcoz we didnot use the getter/setter or property decorator (get_balance fn is getter here)

        


#               =================  Property decorators  ======================

# class Temperature:
#     def __init__(self,celsius=0):
#         self.__celsius=celsius

#     @property                       # ______
#     def celsius(self):              #      |===> Getters
#             return self.__celsius   # _____|


#     @celsius.setter
#     def celsius (self,value):                                      # _______
#             if value< -273.15:                                     #       |
#                 raise ValueError("Below Absolute Zero!")           #      |===> Setters
#             self.__celsius=value                                  # _____|

#     @property
#     def fahrenheit(self):
#             return self.__celsius*(9/5)+32




# #_________  object creation  ___________

# t=Temperature(25)
# print(t.celsius)           # <-- no ()  needed
# print(t.fahrenheit)

# t.celsius =100
# print(t.fahrenheit)



# #               =================  Name Mangling ======================

# class MyClass:
#     def __init__(self):
#         self.public="anyone"
#         self._protected="inside the class"
#         self.__private="outside the class"

# obj=MyClass()
# print(obj.public)       #can be accessed anywhere 
# print(obj._protected)   # can be accessed inside the class only
# # print(obj.private)    # AttributeError => bcoz we didnot use the getter/setter or property decorator 

    
# # _____________ Python Mangles (__private to => _MyClass__private) _____________ 

# print(obj._MyClass__private)

# # _____________ Checking with dir() ________________

# attrs=[a for a in dir(obj) if not a.startswith("__")]
# print(attrs)


#               =================  Class Methods And Static Methods ======================

class Employee:
    company = "KRM Corp"            # class variable
    _count = 0                      # protected class variable


    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
        Employee._count+=1



    @classmethod
    def get_count(cls):                               # it recieves class(here Employee) , not instance(no value is passed as attributes while calling this fn.)
        return f"{cls.company} has {cls._count} employees"


    @staticmethod
    def validate_dept(dept):     # no cls or self needed (helper function that performs a task but doesn't need any data from a specific object (self) or the class (cls).)
        valid = ["CSE","ESE","MBA","MCA"]
        return dept in valid

e1 =Employee("Alice","CSE")
e2 = Employee("Bob","ECE")
print(Employee.get_count())
print(Employee.validate_dept("CSE")) 

#_________or we can use  _____________  
# print(e1.validate_dept("CSE"))






