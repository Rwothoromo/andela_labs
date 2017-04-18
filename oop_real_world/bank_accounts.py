class BankAccount(object):
    """ Manage different types of Bank Accounts """

    def __init__(self, name,  balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # def withdraw(self, amount):
    #     if amount > self.balance:
    #         raise RuntimeError('Amount greater than available balance.')
    #         self.balance -= amount
    #     return self.balance


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 20000


class CurrentAccount(BankAccount):
    def __init__(self):
        pass
