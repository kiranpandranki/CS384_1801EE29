# Function to add two numbers
def add(num1, num2):
    if not(type(num1) is int or type(num1) is float or type(num1) is complex):
        return 0
    elif not(type(num2) is int or type(num2) is float or type(num2) is complex):
        return 0
    addition = num1 + num2
    addition = round(addition.real, 3) + round(addition.imag, 3)*1j
    return addition

# Function to subtract two numbers


def subtract(num1, num2):
    if not(type(num1) is int or type(num1) is float or type(num1) is complex):
        return 0
    elif not(type(num2) is int or type(num2) is float or type(num2) is complex):
        return 0
    subtraction = num1 - num2
    subtraction = round(subtraction.real, 3) + round(subtraction.imag, 3)*1j
    return subtraction

# Function to multiply two numbers


def multiply(num1, num2):
    if not(type(num1) is int or type(num1) is float or type(num1) is complex):
        return 0
    elif not(type(num2) is int or type(num2) is float or type(num2) is complex):
        return 0
    multiplication = num1 * num2
    multiplication = round(multiplication.real, 3) + \
        round(multiplication.imag, 3)*1j
    return multiplication

# Function to divide two numbers


def divide(num1, num2):
    if not(type(num1) is int or type(num1) is float or type(num1) is complex):
        return 0
    elif not(type(num2) is int or type(num2) is float or type(num2) is complex):
        return 0
    elif num2 == 0:
        return 0
    division = num1 / num2
    division = round(division.real, 3) + round(division.imag, 3)*1j
    return division


# Function to add power function
# You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2):  # num1 ^ num2
    power = 1
    if not(type(num1) is int or type(num1) is float):
        return 0
    elif type(num2) is not int:
        return 0
    for i in range(num2):
        power *= num1
    return round(power, 3)

# Python 3 program to print GP.  geometric Progression
# You cant use the inbuilt python function. Write your own function


def printGP(a, r, n):
    gp = []
    if n <= 0 or type(n) != int:
        return 0
    elif not(type(a) is int or type(a) is float):
        return 0
    elif not(type(r) is int or type(r) is float):
        return 0
    multiplier = 1
    for i in range(n):
        gp.append(round(a * multiplier, 3))
        multiplier *= r
    return gp

# Python 3 program to print AP.  arithmetic Progression
# You cant use the inbuilt python function. Write your own function


def printAP(a, d, n):
    adder = 0
    ap = []
    if n <= 0 or type(n) != int:
        return 0
    elif not(type(a) is int or type(a) is float):
        return 0
    elif not(type(d) is int or type(d) is float):
        return 0
    for i in range(n):
        ap.append(round(a + adder, 3))
        adder += d
    return ap

# Python 3 program to print HP.   Harmonic Progression
# You cant use the inbuilt python function. Write your own function


def printHP(a, d, n):
    adder = 0
    hp = []
    if n <= 0 or type(n) != int:
        return 0
    elif not(type(a) is int or type(a) is float):
        return 0
    elif not(type(d) is int or type(d) is float):
        return 0
    for i in range(n):
        if a + adder is 0:
            return 0
        hp.append(round(1/(a + adder), 3))
        adder += d
    return hp
