class BankAccount(object):
    """ Manage different types of Bank Accounts """

    def __init__(self, name, account_type, balance=0.0):
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance



class SavingsAccount(BankAccount):
    def __init__(self, name):
        self.balance = 25000
        self.account_type = "Savings Account"


class CurrentAccount(BankAccount):
    def __init__(self, name):
        self.account_type = "Current Account"
