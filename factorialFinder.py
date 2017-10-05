# Created on Oct. 5, 2017 by @alessiawilliams on GitHub

import math
import str

# Factorial Finder:
# The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2,
# ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.

# Simply, this could be achieved using:
tempInt = 12
math.factorial(tempInt)
# ...which would return 479001600.

# With a recursive loop, however (assuming the user will always enter an integer):
def fact_func(f):
    if(f == 1):
        return(1)
    else:
        return(f * fact_func(f - 1))

usrNum = int(input("Enter a number >=1: "))
print(fact_func(usrNum))
# This simply refers back to itself, multiplying it by itself -1.
