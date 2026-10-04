# 1. Import entire module
import math
print("Using import math:", math.sqrt(25))

# 2. Import with alias
import math as m
print("Using alias:", m.sqrt(36))

# 3. Import specific function
from math import factorial
print("Using from import:", factorial(5))

# 4. Import multiple functions
from math import pow, ceil
print("Using multiple imports:", pow(2, 3))
print("Ceil value:", ceil(4.2))