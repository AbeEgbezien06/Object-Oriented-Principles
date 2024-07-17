class Account:

    def __init__(self):
        self.balance = 10000
        print("Account balance is: ", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Account balance is: ", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Account balance is: ", self.balance)




# Create an instance of the Account class
my_account = Account()

# Perform some operations
my_account.deposit(500)
my_account.withdraw(200)

class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

current = CurrentAccount()
current.withdraw(2000)


class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def savingsWithdraw(self, amount):
        if (amount < 1000):
            super().withdraw(amount)
        else:
            print("Amount exceeds withdrawal limit")


savings = SavingsAccount()
savings.savingsWithdraw(2000)

