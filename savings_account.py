# POLYMORPHISM
#  is when both the parent and child class
# have the same  names, there by allowing us to have
# two seperate execution of the methods

from account import Account ;

class SavingsAccount2(Account):
    #def __init__(self):
    #    Account.__init__(self)

    def withdraw(self, amount):
        if(amount < 1000):
            super().withdraw(amount)
        else:
            print("Amount exceeds withdrawal limit")

savings = SavingsAccount2()
savings.withdraw(1000)