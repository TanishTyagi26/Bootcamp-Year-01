#====================== LAMBDA FUNCTIONS =============================


#--------regular function ------------
def square(x):
        return x*x
square(5)

#-----------lambda function------------
square = lambda x : x*x
print(square(5))


#__________________________ Lambda with Map()_________________________


########IMPORTANT : we always covert the data into the LIST while using map,filter,sorted
no=[1,2,3,4,5]
# Using map() with Lambda

squares=list(map(lambda x : x**2 , no))
print(squares)#-> [1,4,9,16,25]


#__________________________ Lambda with Filter()_________________________

num=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x: x%2==0 , num))   #-> [2,4,6,8,10]


#__________________________ Lambda with Sorted()_________________________
students=[("Alice",85),
        ("Bob",72),
        ("Eve",90)]
#sort by Score in  descending order
r=sorted(students ,
        key = lambda x: x[1], 
        reverse=True)

#__________________________ Nested Lambda _________________________

multiplier= lambda n :(lambda x: x*n)
double = multiplier(2)
triple = multiplier(3)
print(double(5))     #-> result 10
print(triple(5))     #-> result 15









































































