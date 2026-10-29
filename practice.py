##Create a class named BankAccount with a private attribute __balance, initialized to zero.

#Define a deposit() method that accepts an amount and adds it to the balance.

#Define a withdraw() method that accepts an amount and deducts it from the balance if sufficient funds are available.

#Define a getBalance() method that returns the current balance.

#Create an object of the BankAccount class.

#Perform deposit and withdrawal operations, display appropriate messages, and print the final balance

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def getBalance(self):
        return self.__balance


# Create an object
account = BankAccount()

# Perform deposit and withdrawal operations
account.deposit(5000)
account.withdraw(2000)

# Display final balance
print("Final balance:", account.getBalance())