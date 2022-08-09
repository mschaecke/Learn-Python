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

variable = random.randrange(1, 100)
print(variable)
print(type(variable))

# Underscore separators can be replaced by a symbol in f-strings
variable = 1_000_000
print(f"{variable:,}")

# Python offers the following seven arithmetic operators to perform
# mathematical operations:

# Addition "+"
# Adds two values

variable = 1 + 1  # variable = 2
print(variable)

# Subtraction "-"
# Subtracts the second value from the first value

variable = 3 - 2  # variable = 1
print(variable)

# Multiplication "*"
# Multiplies two values to find the product

variable = 2 * 3  # variable = 6
print(variable)

# Division "/"
# Divides the first operand by the second to find the quotient
# Division always returns a float
# Use int() to return an integer

variable = 9 / 3  # variable = 3.0
print(variable)

variable = int(9 / 3)  # variable = 3
print(variable)

# Floor division "//"
# Divides the first operand by the second to find the floor of the quotient
# (rounding down to the nearest integer)

variable = 7 // 3  # variable = 2
print(variable)

# Modulus "%"
# Divides the first operand by the second to find the remainder

variable = 7 % 3  # variable = 1
print(variable)

# Exponents "**"
# Raises the first operand to the power of the second (exponent)

variable = 10 ** 3  # variable = 1000
print(variable)

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
