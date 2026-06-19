# Simple ATM

correct = 1234
pin = int(input("Enter your 4 digit PIN : "))
if pin == correct:
    withdraw = float(input("Enter the withdrawal amount : "))
    if withdraw <=5000:
        print("Dispensing Cash.......")
    else:
        print("Limit Exceeded!!!")
else:
    print("Invalid PIN")