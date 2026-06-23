# Build a simple BankAccount class supporting deposits and withdrawals

# Create a class BankAccount with an instance attribute balance (set manually to O after creation). Add methods deposit (amount) that increases balance and withdraw(amount) that decreases it only if sufficient funds exist (otherwise print an error). Create two accounts and perform several operations, printing the balance after each.



class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"{amount} deposited successfully...")
        print(f"Balanced Amount is : {self.balance}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(f"{amount} withdrawed successfully...")
            print(f"Balanced Amount is : {self.balance}\n")
        else:
            print("Sorry !!!!!!\tthe amount is not sufficient...")
            print(f"Balanced Amount is : {self.balance}")

acc1=BankAccount()
acc1.deposit(1000)
acc1.withdraw(156)

acc2=BankAccount(100)
acc2.deposit(50)
acc2.withdraw(50000)