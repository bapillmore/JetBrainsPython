import math


def new_math_factorial(n):
    return print("Don't cheat!")


math.factorial = new_math_factorial


# don't delete this line, please
math.factorial(23)
