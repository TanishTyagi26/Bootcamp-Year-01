#=================  personal expense tracker ====================
# accept : food expense ,travel expense ,internet bill , entertainment expense ,miscellaneous expense 
# Calculations : total expense,remainining balance,percentage spent  
# output : monthly budget ,total expense,balance left , spent percentage 
#extension : display warning if spending exceeds 80% .

def personal_expense_tracker(budget):
    total_expense = food_expense +food_expense + internet_bill+entertainment_expense+miscellaneous_expense
    balance_left = budget - total_expense
    spent_percentage = (total_expense/budget)*100
    if spent_percentage >= 80:
        print(f"your expenses are exceeding with the percentage of {spent_percentage}")

    print(f"Your Monthly Budget is : {budget}")
    print(f"Total Expense : {total_expense}")
    print(f"Balance Left : {balance_left}")
    print(f"Spent Percentage : {spent_percentage}%")


print("=================  personal expense tracker ====================")
budget = int(input("enter your monthly budget :"))
food_expense = int(input("enter your Food expense :"))
food_expense  = int(input("enter your Travel expense :"))
internet_bill = int(input("enter your Internet Bill :"))
entertainment_expense = int(input("enter your entertainment expense :"))
miscellaneous_expense = int(input("enter your miscellaneous expense :"))

personal_expense_tracker(budget)

