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
    balance = 25000
    account_type = "Savings Account"


class CurrentAccount(BankAccount):
    account_type = "Current Account"
