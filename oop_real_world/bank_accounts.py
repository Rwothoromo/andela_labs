class BankAccount(object):
    """ Manage different types of Bank Accounts """
    
    def __init__(self, name):
        self.name = name
    
    def set_balance(self, balance=0.0):
        self.balance = balance
    
    # def withdraw(self, amount):
    #     if amount > self.balance:
    #         raise RuntimeError('Amount greater than available balance.')
    #         self.balance -= amount
    #     return self.balance

    # def deposit(self, amount):
    #     self.balance += amount
    #     return self.balance
T
class SavingsAccount():


class CurrentAccount():
