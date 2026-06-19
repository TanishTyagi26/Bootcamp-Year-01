# ________________________map()___________________________

#wap to square all no. in a list

# num=[1,2,3,4,5,6,7,8,9,10]
# square= list(map(lambda x:x**2 ,num))
# print(square)

#wap to convert temp from  celsius to fahrenheit  in a list
# celsius_temperature=[25, 100, 0, 20, 30, 40]
# fahrenheit_temperature=list(map(lambda x :(x*1.8)+32,celsius_temperature) )
# print(fahrenheit_temperature)


#wap to convert all no.s to uppercase
# lst=["tanish","ayush","rahul","anik","aryan"]
# uppercase=list(map(lambda x: x.upper(),lst))
# print(uppercase)



#wap to find the length of the all characters in list 
# list1=["tanos","sgdh","shugijok","hfrgfhsd"]
# length=list(map(lambda x: len(x),list1))
# print(length)

# ________________________filter()___________________________



#wap to keep only  even no.

# num=[]
# for i in range(1,100):
#     num.append(i)

# even_num=list(filter(lambda x: x%2 ==0 ,num))
# print(even_num)

#wap to keep only  even no.


# lst=["Aman", "Rahul", "Priyanka", "Tanish"]
# name_longer=list(filter(lambda x: len(x)>5,lst))
# print(name_longer)

# filter positive num. only

# lst=[-5, 3, -1, 10, 0, 8]
# positive_num=list(filter(lambda x: x>=0,lst))
# print(positive_num)

# Keep numbers divisible by both 3 and 5 in range (1-100)

# nums=[]
# for i in range(1,101):
#     nums.append(i)

# multiples_of_5_and_3=list(filter(lambda x : x%3==0 or x%5==0,nums))
# print(multiples_of_5_and_3)

# ________________________filter()___________________________



# Find sum of all numbers
from functools import reduce
lst=[10,20,30,40]
sum_lst=reduce(lambda x,y:x+y ,lst)
print(sum_lst)



    












































































