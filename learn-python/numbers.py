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
