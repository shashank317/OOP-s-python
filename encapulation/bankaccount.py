class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def show_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Balance: ${self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if amount <=self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds for withdrawal.")

acc = BankAccount("Shashank", 1000)
acc.show_balance()
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()

# Trying to access balance directly (this won't work)
# print(acc.__balance)  ❌ will give error
