# __________________Bank Account Simulator________________________

# Create a BankAccount class with deposit() and withdraw() methods. Define custom exceptions: Insufficient FundsError and InvalidAmountError. Test with a series of valid and invalid transactions.

# Hint: Raise exceptions inside class methods; catch them in a transaction loop

class InsufficientFundsError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than 0.")

        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than 0.")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance.")

        self.balance -= amount
        print("Withdrawn:", amount)


account = BankAccount()

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            print("Current Balance:", account.balance)

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")

    except InvalidAmountError as e:
        print("Error:", e)

    except InsufficientFundsError as e:
        print("Error:", e)