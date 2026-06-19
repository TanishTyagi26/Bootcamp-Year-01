#wap to ask for monthly income and existing EMIs
# conditions to print in each case : if income>=30,000 and EMI <0.4*income --> "eligible for loan" -------------- if income <30,000-->"income too low"------------------- if EMI >=0.4*income --> "high debt burden" 


def loan_eligible(income,emi):
    if income>=30000 :
        if emi< (0.4 * income):
            print("eligible for loan ...")
    elif income<30000:
        print("income too low...")
    elif emi >=(0.4*income):
        print("high debt burden ...")

income=int(input("enter your monthly income : "))
emi = int(input("enter your EMI:"))
loan_eligible(income,emi)
