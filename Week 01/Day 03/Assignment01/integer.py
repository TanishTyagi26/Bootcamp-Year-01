#wap to check whether the input is positive , negative or zero . using if , else, elif .test the program at leats 5 different inputs including boundary value  0 .



def check_integer(value):
    if value > 0 :
        print(f"{value} : is an positive Number .")
    elif value < 0 :
        print(f"{value} : is an negative Number .")
    else :
        print(f"{value} : is ZERO  .")

while True :
    print(f"Enter your choice Below ")
    choice = str (input("[y/n] :"))

    if choice == "y" :
        value = float(input("enter your value : "))
        check_integer(value)
    else :
        print("exiting the program ....")
        print("===============================================================")
        break 

# print(f"Do You want to run the program ....")
