# creating an acccount using functions
def make_account():
    return {'balance': 0}


def deposit(account, amount):
    account['balance'] += amount
    return account['balance']


def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

"""
a = make_account()
b = make_account()
deposit(a, 100)
100
deposit(b, 50)
50
withdraw(a, 10)
90
withdraw(b, 10)
40
"""

# creating an account using classes
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

"""
a = BankAccount()
b = BankAccnout()
a.deposit(100)
100
b.deposit(50)
50
a.withdraw(10)
90
b.withdraw(10)
40
"""

# Inheritance:
class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)
            return self.balance

"""
b = MinimumBalanceAccount(10)
b.deposit(10)
10
b.deposit(10)
20
b.withdraw(10)
10
"""
# What does a class inherit? All methods?
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

"""
a = A()
b = B()
print(a.f())
A
print(b.f())
B
print(a.g())
A
print(b.g())
B
"""

