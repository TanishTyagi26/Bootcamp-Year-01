#attributes , data , characteristics, properties => stored in variables
#methods , functions , behaviors 


#Class Attributes
class Dog :
    species = "Canine"  # Class Attribute(shared by all objects)

    def bark (self):
        print("woof!")

Jackie=Dog()        # Created an object named Jackie
Jackie.bark()       # Called the method named bark()




#   Instance attribute : are set using dot notation (object.attribute = value) and belong to ONE specific object only .

class Dog:
    def set_name(self,n):
        self.name=n  # Instance Attribute (shared by specific objects \ meaning name can be anything)

rex=Dog()
rex.set_name("Rex")
# self becomes rex automatically


# self => it refers to the specific object  a method is being called on.
#   it's how a method knows which object's data is being read or modify.
#       self is always first parameter of any  method inside a class
#       python passes it automatically  - you never type it when calling a method
#       self.name means "this particular object's name attribute"
#       you can name it anything , but self is the universal Python convention.
