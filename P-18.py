# 8. Write a program to illustrate variable scope using local global and nonlocal variables. 

x = 10

def outer():
    y = 20

    def inner():
        z = 30

        print("Global variable:", x)
        print("Nonlocal variable:", y)
        print("Local variable:", z)

    inner()

outer()

print("Outside function - Global variable:", x)