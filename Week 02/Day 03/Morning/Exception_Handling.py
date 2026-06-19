

#__________________________ Exception Handling_________________________


try :
    num=int(input("enter a no. : "))
    result = 100/num
    print(f"Result : {result}")
except ZeroDivisionError :
    print("Error : Divided By Zero")
except ValueError:
    print("Error : Enter Valid Input")




















