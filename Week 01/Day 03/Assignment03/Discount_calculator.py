#wap for Discount calculator for E-Commerce website using  nested (if -else- elif): :
#conditions : 


cart = float(input("Enter the original price of cart : "))

if cart > 5000:
    prem = input("Are you a premium user [y/n] : ")
    if prem.lower() == 'y':
        print(f"Original Price : {cart}")
        print(f"Discount 20% : {cart*0.2}")
        print(f"Final Price : {cart-(cart*0.2)}")
    else:
        print(f"Original Price : {cart}")
        print(f"Discount 15% : {cart*0.15}")
        print(f"Final Price : {cart-(cart*0.15)}")
else:
    print(f"Original Price : {cart}")
    print(f"Discount 5% : {cart*0.05}")
    print(f"Final Price : {cart-(cart*0.05)}")