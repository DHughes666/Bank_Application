"""4-Bank Account Manager - Create a class called Account which will be an abstract
class for three other classes called CheckingAccount, SavingsAccount and BusinessAccount.
Manage credits and debits from these accounts through an ATM style program."""

from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @abstractmethod
    def accBalance(self):
        print("***ACCOUNT BALANCE***")


class CheckingAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def accBalance(self):
        super().accBalance()
        return self.balance

    def acc_type(self):
        accType = input('Savings or Business? ')
        if accType.upper().startswith('S'):
            ans = 'SAVINGS ACCOUNT'
        else:
            ans = 'BUSINESS ACCOUNT'
        return ans


class SavingsAccount(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance)
        print('Welcome {}\nAccount Type : SAVINGS'.format(self.name))

    def accBalance(self):
        super().accBalance()
        print("FOR SAVINGS ACCOUNT {}".format(
            self.balance + (self.balance * 0.1)))

    def deposit(self, amt):
        self.balance += amt 
        print('You have deposited ', amt)
        print('Main balance is ', self.balance)

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print('Withdraw successful')
        else:
            print('Insufficient fund')


class BusinessAccount(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance)
        print('Welcome {}\nAccount Type : BUSINESS'.format(self.name))

    def accBalance(self):
        super().accBalance()
        print("FOR BUSINESS ACCOUNT {}".format(
            self.balance + (self.balance * 0.25)))

    def deposit(self, amt):
        self.balance += amt
        print('You have deposited ', amt)
        print('Main balance is ', self.balance)

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print('Withdraw successful')
        else:
            print('Insufficient fund')
