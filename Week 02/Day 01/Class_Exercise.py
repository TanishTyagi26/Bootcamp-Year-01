
# x=3
# y=10
# if x<y :
#     print("y is greater than x")




# #wap to find the max among the two no.
# # num1= int(input("enter your first number :"))
# # num2= int(input("enter your second number :"))
# # if num2 >num1 :
# #     print(f"{num2} is greater than {num1}")
# # else:
# #     print(f"{num1} is greater than {num2}")


# #ques 2 wap that takes input any no. and adds 7 if odd else add 4
# num= int(input("enter your number :"))

# if num%2==0 :
#     print(f"{num} is even ")
#     print(f"{num + 4}")
# else:
#     print(f" {num} is odd")
#     print(f"{num + 7}")


# #ques 3 wap to create a simple number guessing game 
# number= int(input("enter your number : "))
# if number == 45 :
#     print(f"congratulations! {number} is the answer")
# elif number>45 :
#     print(f"your guessed number is greater {number-45}than the answer  ")
# else:
#     print(f"your no. is smaller {45-number} than the answer")

# #ques3 chatgpt answer
# import random

# # Numbers and their weights
# numbers = [1, 2, 3, 4, 5]
# weights = [10, 20, 30, 25, 15]

# # Roulette wheel selection
# secret_number = random.choices(numbers, weights=weights, k=1)[0]

# print("Guess a number between 1 and 5")

# # while True:
# #     guess = int(input("Enter your guess: "))

# #     if guess == secret_number:
# #         print("Congratulations! You guessed correctly.")
# #         break
# #     else:
# #         print("Wrong guess. Try again!")


# num=5
# if num >=0:
#     if num ==0 :
#         print("no. is zero ")
#     else:
#         print("no. is positive")
# else:
#     print("no. is negative")





# _______________________________________________________________________________



# if (a>b):
#     if a>c:
#         print("A is max ")
#     else:
#         print("C is max")
# else:
#     if b>c :
#         print("B is max")
#     else:
#         print(" C is max")


# ________________________________________________________________
# while True:
#     num = int(input("enter your  number :"))
#     if num >=0:
#         if num ==0 :
#             print("no. is zero ")
#         else:
#             print("no. is positive")
#             if num%2 == 0:
#                 print(f"{num } is even no.")
#             else:
#                 print(f"{num} is odd")
#     else:
#         print("no. is negative")
#         if num%2 == 0:
#                 print(f"{num } is even no.")
#         else:
                # print(f"{num} is odd")


# ________________________________________________________________
# while True:
#     num1 = int(input("enter your first  number :"))

#     num2 = int(input("enter your second number :"))
#     num3 = int(input("enter your  third number :"))
#     if (num1>num2):
#         if num1>num3:
#             print(f"{num1} is max. ")
#         else:
#             print(f"{num3} is max. ")
#     else:0
#         if num2>num3 :
#             print(f"{num2} is max. ")
#         else:
#             print(f"{num3} is max. ")

# ________________________________________________________________
# while True:
#     score = float(input("enter your score: "))
#     if score >=90 and score <=100 :
#         print(f"grade is : A")
#     elif score >=80 and score <=89 :
#         print(f"grade is : B")
#     elif score >=70 and score <=79 :
#         print(f"grade is : C")
#     elif score >=60 and score <=69 :
#         print(f"grade is : D")
#     elif score <69 :
#         print(f"grade is : F")
#     else:
#         print("invalid input")
# ________________________________________________________________


# for i in range (1,11):
#     for j in range(1,11):
#         print(i*j , end="\t")
#     print()

#----------------- or -----------------------

# num = 1
# while num <=10:
#     i = 1
#     while i<=10:
#         print(num * i , end="\t")
#         i+=1
#     print("\n")
#     num+=1


# ________________________________________________________________

# lst=[2,4,5,6,7,8,9,10]
# for i in lst :
#     print(i*i,end=" ")

# ________________________________________________________________
# sum=0
# i=1
# while i<=50 :
#     if (i%2) !=0 :
#         sum+=i
# i+=1
# print(sum)


# ________________________________________________________________




# for i in range(51):
#     if (i%7) == 0 :
#         continue 
#     print(i ,end=" ")
    
# ________________________________________________________________

    
#wap to add number entered by user
# u = input("Enter numbers separated by commas: ").split(",")
# sum = 0
# for item in u:
#     num = int(item.strip())
    
#     if num % 2 == 0:
#         sum = sum+num
# print("The sum of even numbers is:", sum)


# ________________________________________________________________

# import random

# count = 0

# while True:
#     num = random.randint(1, 10)  # generates a number from 1 to 10
#     count += 1
#     print(num)

#     if num > 7:
#         break

# print("Number is:", num)
# print("Total numbers generated:", count)

# ________________________________________________________________

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(f"{fact(5) } : is the factorial of 5")

# ________________________________________________________________
# def temperature_converter(temp, choice):
#     if choice == 1:
#         return (temp * 9 / 5) + 32  # Celsius to Fahrenheit
#     elif choice == 2:
#         return (temp - 32) * 5 / 9  # Fahrenheit to Celsius
#     else:
#         return "Invalid choice"

# choice = int(input("Enter 1 for C→F and 2 for F→C: "))
# temp = float(input("Enter temperature: "))

# print(temperature_converter(temp, choice))

# ________________________________________________________________
# wap to detect a pallindrome text 
# while True:
#     Word = input("Enter a string: ")

#     if Word == Word[::-1]:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")

# ________________________________________________________________
#wap for fibonacci series
# def fib(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fib(num - 1) + fib(num - 2)

# while True:
#     n = int(input("Enter your number: "))
#     if n < 0:
#         print("Please enter a non-negative number")
#     else:
#         print(fib(n))

# ________________________________________________________________








