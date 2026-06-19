# wap to check if the given input year is leap or not 
# logic conditions are : if year (input) is divisible by 4 or 400 then its leap and not divisible by 100.



def leap_year(year):
    if year%4 == 0 :
        print(f"{year} is a leap year ")
    else :
        print(f"{year} is not a leap year ")
    print("If u want to check another year input 'y' ")
    choice = str(input("[y/n]"))
    if choice == "y":
        year= int(input("enter year :"))
        leap_year(year)

    else:
        print("exiting the program ....")

year= int(input("enter year :"))
leap_year(year)