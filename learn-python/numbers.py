import random

# Python has three numeric data types (int, float, complex)

# Integers (int) are whole numbers without decimals
# They can be positive or negative and have no length limit

variable = 1
print(variable)
print(type(variable))

variable = -42
print(variable)

# Integer constructor function
# Converts integer, float (remove decimals) or string to integer
# This example shows integer to integer

variable = int(1_000_000)  # Underscores can be used as separators
print(variable)
print(type(variable))

# This examples shows float to integer

variable = int(2.3)  # variable = 2
print(variable)
print(type(variable))

# This example shows string to int

variable = int("42")  # variable = 42
print(variable)
print(type(variable))

# Floating point numbers (float) contain at least one decimal
# They can be positive or negative
# The power of 10 is indicated via "e" (e.g. print(3e2) = 300.0)

variable = 1.0
print(variable)
print(type(variable))

variable = -42.12345
print(variable)

variable = 3e2  # variable = 300.0
print(variable)

variable = 4E5  # variable = 400000.0
print(variable)

variable = -42.5e10  # variable = -425000000000.0
print(variable)

# Float constructor function
# Converts integer, float or string (integer or float) to float
# This example shows integer to float

variable = float(42)  # variable = 42.0
print(variable)
print(type(variable))

# This examples shows float to float

variable = float(1_234_567.89)  # variable = 1234567.89
print(variable)
print(type(variable))

# This examples shows string (integer) to float

variable = float("42")  # variable = 42.0
print(variable)
print(type(variable))

# This examples shows string (float) to float

variable = float("42.123")  # variable = 42.123
print(variable)
print(type(variable))

# Complex numbers (complex) utilize a "j" for the imaginary number

variable = 4j  # variable = 4j
print(variable)
print(type(variable))

variable = -4j + 2j  # variable = -2j
print(variable)

# Complex constructor function

variable = complex(1j)  # variable = 1j
print(variable)
print(type(variable))

# Data types can be converted to another type via constructor functions

# Conversion from int to float

variable = 1  # int
print(variable)

variable = float(variable)  # float
print(variable)

# Conversion from int to complex

variable = 1  # int
print(variable)

variable = complex(variable)  # complex
print(variable)

# Conversion from float to int

variable = 1.0  # float
print(variable)

variable = int(variable)  # int
print(variable)

# A random number can be generated via Python's built-in "random" module
# Notice the "import random" at the top of this .py file (module)

# Random int between 1 and 100

variable = random.randint(1, 100)
print(variable)
print(type(variable))

# Random int between 1 and 99 (100 is excluded)

variable = random.randrange(1, 100)
print(variable)
print(type(variable))

# Random int between 0 and 99 (100 is excluded) with step 2

variable = random.randrange(0, 100, 2)
print(variable)
print(type(variable))

# Random float between 0 and 1

variable = random.random()
print(variable)
print(type(variable))

# Random element from a non-empty sequence

numbers = [1, 2, 4, 42, 100, 3, 7]
choice = random.choice(numbers)
print(choice)
print(type(choice))

numbers = (1, 2, 4, 42, 100, 3, 7)
choice = random.choice(numbers)
print(choice)
print(type(choice))

# Underscore separators can be replaced by a symbol in f-strings
variable = 1_000_000
print(f"{variable:,}")

# Python offers the following seven arithmetic operators to perform
# mathematical operations:

# Addition "+"
# Adds two values

print(1 + 1)  # Output = 2

# Subtraction "-"
# Subtracts the second value from the first value

print(3 - 2)  # Output = 1

# Multiplication "*"
# Multiplies two values to find the product

print(2 * 3)  # Output = 6

# Division "/"
# Divides the first operand by the second to find the quotient
# Division always returns a float
# Use int() to return an integer

print(9 / 3)  # Output = 3.0

print(int(9 / 3))  # Output = 3

# Floor division "//"
# Divides the first operand by the second to find the floor of the quotient
# (rounding down to the nearest integer)

print(7 // 3)  # Output = 2

# Modulus "%"
# Divides the first operand by the second to find the remainder

print(7 % 3)  # Output = 1

# Exponent "**"
# Raises the first operand to the power of the second (exponent)

print(10 ** 3)  # Output = 1000

# The operator precedence is:
#   brackets
#   exponents
#   division
#   multiplication
#   floor division
#   modulus
#   addition
#   subtraction

# https://docs.python.org/3/reference/expressions.html#operator-precedence

# Brackets (parentheses) can be used to change the operator precedence:

variable = 3 + 2 * 10  # variable = 23
print(variable)

variable = (3 + 2) * 10  # variable = 50
print(variable)

# The arithmetic operators can be used while assigning values to variables

# Addition
# Frequently referred to as incrementing a value

variable = 1
variable += 1  # variable = 2
print(variable)

# Subtraction
# Frequently referred to as decrementing a value

variable = 2
variable -= 1  # variable = 1
print(variable)

# Multiplication

variable = 2
variable *= 3  # variable = 6
print(variable)

# Division

variable = 6
variable /= 3  # variable = 2.0
print(variable)

# Floor division

variable = 7
variable //= 3  # variable = 2
print(variable)

# Modulus

variable = 7
variable %= 3  # variable = 1
print(variable)

# Exponent

variable = 10
variable **= 3  # variable = 1000
print(variable)

# Additionally, Python offers the following mathematical functions:

# Absolute
# Returns the absolute value of a number

print(abs(-42))  # Output = 42

# Sum
# Returns the sum of the function input
# (function arguments corresponding to the function parameters)

number_list = [1, 2, 3]
print(sum(number_list))  # Output = 6

# Maximum
# Returns the largest number

number_list = [7, 42, 1, 23]
print(max(number_list))  # Output = 42

# Minimum
# Returns the smallest number

number_list = [7, 42, 1, 23]
print(min(number_list))  # Output = 1

# Divmod
# Returns both the quotient and remainder of a division as a tuple

print(divmod(5, 3))  # Output = (1, 2)

print(divmod(5.5, 3))  # Output = (1.0, 2.5)

# Round
# Returns an integer by rounding a floating-point number
# Both rounding up and down are possible

print(round(42.89))  # Output = 43

print(round(42.49))  # Output = 42

# Power
# Raises the first number to the power of the second (exponent)

print(pow(10, 3))  # Output = 1000

# Modulus can be used as well (base, exponent, modulus)

print((pow(10, 3, 3)))  # Output = 1

# A sequence of integers can be generated via the range() function
# Float is not supported
# Range is a data type similar to sets or tuples

variable = range(10)  # Range from 0 to 9 (10 is not included)
print(variable)  # Output = range(0, 10)
for value in variable:
    print(value)  # Prints values from 0 to 9
print(type(variable))

# range() can be called with one argument (stop)

variable = range(5)  # Range from 0 to 4 (5 is not included)
for value in variable:
    print(value)  # Prints values from 0 to 4

# range() can be called with two arguments (start, stop)

variable = range(5, 9)  # Range from 5 to 8 (9 is not included)
for value in variable:
    print(value)  # Prints values from 5 to 8

# range() can be called with three arguments (start, stop, step)
# The default step value is 1
# Step must not be 0

variable = range(1, 10, 2)  # Range from 1 to 10 using a step of 2
for value in variable:
    print(value)  # Prints the values 1, 3, 5, 7 and 9

# Negative step values are possible as well

variable = range(10, 0, -2)  # Range from 10 to 0 using a step of 2
for value in variable:
    print(value)  # Prints the values 10, 8, 6, 4 and 2 (0 not included)

# Negative values for start and stop work too

variable = range(-10, -20, -3)
for value in variable:
    print(value)  # Prints the values -10, -13, -16 and -19

# Items can be accessed by the index value similar to a list

variable = range(5)

print(variable[0])  # Prints the first element 0
print(variable[4])  # Prints the last element 4
print(variable[-2])  # Prints the fourth element 3

# range() is frequently used in for loops

for i in range(1, 5):
    print(i)  # Prints values from 1 to 4
