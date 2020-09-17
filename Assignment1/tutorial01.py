# Function to add two numbers
def add(num1, num2):
    if not isinstance(num1, (int, float)):
        return 0
    if not isinstance(num2, (int, float)):
        return 0
    addition = num1 + num2
    return round(addition, 3)

# Function to subtract two numbers


def subtract(num1, num2):
    if not isinstance(num1, (int, float)):
        return 0
    if not isinstance(num2, (int, float)):
        return 0
    subtraction = num1 - num2
    return round(subtraction, 3)

# Function to multiply two numbers


def multiply(num1, num2):
    if not isinstance(num1, (int, float)):
        return 0
    if not isinstance(num2, (int, float)):
        return 0
    multiplication = num1 * num2
    return round(multiplication, 3)

# Function to divide two numbers


def divide(num1, num2):
    if not isinstance(num1, (int, float)):
        return 0
    if not isinstance(num2, (int, float)):
        return 0
    if num2 == 0:
        return 0
    division = num1 / num2
    return round(division, 3)


# Function to add power function
# You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2):  # num1 ^ num2
    power = 1
    if not isinstance(num1, (int, float)):
        return 0
    if not isinstance(num2, (int, float)):
        return 0
    if int(num2) != num2:
        return 0
    else:
        for i in range(abs(int(num2))):
            power *= num1
    if num2 < 0:
        return round(1/power, 3)
    else:
        return round(power, 3)

# Python 3 program to print GP.  geometric Progression
# You cant use the inbuilt python function. Write your own function


def printGP(a, r, n):
    gp = []
    multiplier = 1
    if not isinstance(a, (int, float)):
        return [0]
    if not isinstance(r, (int, float)):
        return [0]
    if not isinstance(n, (int, float)):
        return [0]
    if isinstance(n, (int, float)):
        if n < 0 or int(n) != n:
            return [0]
    for i in range(int(n)):
        gp.append(round(a * multiplier, 3))
        multiplier *= r
    return gp

# Python 3 program to print AP.  arithmetic Progression
# You cant use the inbuilt python function. Write your own function


def printAP(a, d, n):
    adder = 0
    ap = []
    if not isinstance(a, (int, float)):
        return [0]
    if not isinstance(d, (int, float)):
        return [0]
    if not isinstance(n, (int, float)):
        return [0]
    if isinstance(n, (int, float)):
        if n < 0 or int(n) != n:
            return [0]
    for i in range(int(n)):
        ap.append(round(a + adder, 3))
        adder += d
    return ap

# Python 3 program to print HP.   Harmonic Progression
# You cant use the inbuilt python function. Write your own function


def printHP(a, d, n):
    adder = 0
    hp = []
    if not isinstance(a, (int, float)):
        return [0]
    if not isinstance(d, (int, float)):
        return [0]
    if not isinstance(n, (int, float)):
        return [0]
    if isinstance(n, (int, float)):
        if n < 0 or int(n) != n:
            return [0]
    for i in range(int(n)):
        if a + adder is 0:
            return [0]
        hp.append(round(1/(a + adder), 3))
        adder += d
    return hp
