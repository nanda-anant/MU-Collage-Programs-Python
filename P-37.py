# Program to demonstrate MRO and Magic Methods

class A:

    def __init__(self):
        print("Constructor of Class A")

    def show(self):
        print("Method of Class A")


class B(A):

    def __init__(self):
        print("Constructor of Class B")
        super().__init__()

    def show(self):
        print("Method of Class B")


class C(A):

    def __init__(self):
        print("Constructor of Class C")
        super().__init__()

    def show(self):
        print("Method of Class C")


class D(B, C):

    def __init__(self):
        print("Constructor of Class D")
        super().__init__()

    def __str__(self):
        return "Object of Class D"


# Creating an object
obj = D()

print("\nMethod Resolution Order:")
print(D.mro())

print("\nCalling show() method:")
obj.show()

print("\nMagic Method __str__():")
print(obj)