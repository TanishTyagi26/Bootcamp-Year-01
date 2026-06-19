#wap to read temp in deg celsius and advise clothes according to the weather 
#conditions : <0degC wear heavy coat ,, 0-15degC wear a jacket ,, 16-30degC comfortable weather,, >30degC wear light  clothing and stay hydrated.



def clothing_Advise(temperature):
    if temperature < 0:
        print(f"Temperature is {temperature}")
        print(f"Wear Heavy Coat")
    elif temperature <=15 :
        print(f"Temperature is {temperature}")
        print(f"Wear a jacket")
    elif temperature<=30:
        print(f"Temperature is {temperature}")
        print(f"comfortable weather")
    elif temperature>30:
        print(f"Temperature is {temperature}")
        print(f"wear light  clothing and stay hydrated.")


temperature= float(input("enter Temperature in degree Celsius : "))
clothing_Advise(temperature)