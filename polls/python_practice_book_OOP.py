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
            print('Sorry, minimum balance must be maintained.')
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

# Another code example of class inheritance:


class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' '] * width for i in range(height)]

    def setpixel(self, row, col):
        self.data[row][col] = '*'

    def getpixel(self, row, col):
        return self.data[row][col]

    def display(self):
        print("\n".join(["".join(row) for row in self.data]))


class Shape:
    def paint(self, canvas):
        pass


class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def hline(self, x, y, w):
        pass

    def vline(self, x, y, h):
        pass

    def paint(self, canvas):
        hline(self.x, self.y, self.w)
        hline(self.x, self.y + self.h, self.w)
        vline(self.x, self.y, self.h)
        vline(self.x + self.w, self.y, self.h)


class Square(Rectangle):
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)


class CompoundShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def paint(self, canvas):
        for s in self.shapes:
            s.paint(canvas)

# Special Class Methods


class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
        >>> a - b
        1/6
        >>> a * b
        1/6
        >>> a/b
        3/2
    """
    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1 * d2 - n2 * d1, d1 * d2)

    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1 * n2, d1 * d2)

    def __div__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1 * d2, d1 * n2)

    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    __repr__ = __str__

    # Errors and Exceptions

try:
    print("a")
except:
    print("b")
else:
    print("c")
finally:
    print("d")

"""
a
c
d
"""

try:
    print("a")
    raise Exception("doom")
except:
    print("b")
else:
    print("c")
finally:
    print("d")

"""
a
b
d
"""


def f():
    try:
        print("a")
        return
    except:
        print("b")
    else:
        print("c")
    finally:
        print("d")

f()

"""
a
d
"""
