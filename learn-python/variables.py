# Variables are containers which store data
# They are created after a value is assigned

x = "Hello"
y = 10
z = True

print(x)
print(y)
print(z)

# A type declaration in not needed in Python
# This happens automatically and can be changed later

print(x)

x = "World"
print(x)

x = 20
print(x)

# The data type can be specified by the user via type casting

x = str(30)
y = int(30)
z = float(30)

# The data type can be checked via type()

print(type(x))  # string '30'
print(type(y))  # integer 30
print(type(z))  # float 30.0

# Use descriptive variable names instead of single characters (most of the time)
# Python is case-sensitive (name != Name)
# The names must start with a letter (NOT number) or underscore
# Use alphanumeric characters or underscores
# Agree upon a naming convention in group projects

name = "Hello"
Name = "World"

print(name)
print(Name)

othervariable = 1
otherVariable = 2  # This is known as camel case
other_variable = 3  # Snake case
_other_Variable = 4
OtherVariable = 5  # Pascal case
OTHERVARIABLE = 6

# Assign different values to multiple variables in a single line

varOne, varTwo, varThree = 1, 2, 3

print(varOne)
print(varTwo)
print(varThree)

# Assign the same value to multiple variables in a single line

varOne = varTwo = varThree = 1

print(varOne)
print(varTwo)
print(varThree)

# This can be used to swap the values of multiple variables as well

a, b, c = 1, 2, 3

print(a, b, c)

a, b, c = c, a, b

print(a, b, c)

# Unpack a collection of values (list, tuple, etc.)
# The values are extracted and assigned to variables

# This works for lists

names = ["Alice", "Bob", "Charlie"]
nameOne, nameTwo, nameThree = names

print(nameOne)
print(nameTwo)
print(nameThree)

# tuples,

numbers = (1, 2, 3)
numberOne, numberTwo, numberThree = numbers

print(numberOne)
print(numberTwo)
print(numberThree)

# strings,

string = "Abc"
stringOne, stringTwo, stringThree = string

print(stringOne)
print(stringTwo)
print(stringThree)

# dictionaries

dictionary = {"A": 1, "B": 2}
keyOne, keyTwo = dictionary  # assign the keys

print(keyOne)
print(keyTwo)

valueOne, valueTwo = dictionary.values()  # assign the values

print(valueOne)
print(valueTwo)

itemOne, itemTwo = dictionary.items()  # assign the items as tuples

print(itemOne)
print(itemTwo)

# and coordinates (which in this case are a list of floats)

coordinates = [1.467, 3.653]
x, y = coordinates

print(x, y)

# Use print() to output a single variable

varOne = 1

print(varOne)

# Use print() to output multiple variables

varOne, varTwo, varThree = "How", "are", "you?"

print(varOne, varTwo, varThree)

# The "+" operator can be used as well (notice the lack of spaces)

print(varOne + varTwo + varThree)

# This does NOT work for numbers because "+" is a mathematical operator
# (addition) in this case

varOne, varTwo, varThree = 1, 2, 3

print(varOne + varTwo + varThree)

# If both a number (e.g. 1) and string (e.g. "Hello") are printed via "+"
# operator, an error occurs
# Use ","  to output multiple variables, especially of different data types

varOne, varTwo = 1, "Hello"

print(varOne, varTwo)

# Local variables are created in a function and can only be used within it
# Global variables are created outside of functions and can be used anywhere

global_variable_one = "Global variable one"


def print_global_variable():
    print(global_variable_one)


print_global_variable()

# If both (local and global functions) exist and share the same name,
# only the local one inside the function is used

global_variable_two = "Global variable two"


def print_local_variable():
    global_variable_two = "Local variable with the same name"

    print(global_variable_two)


print(global_variable_two)
print_local_variable()


# Create global variables within functions via the "global" keyword

def create_global_variable():
    global global_variable_three
    global_variable_three = "Global variable three created within a function"

    print(global_variable_three)


create_global_variable()

# Modify global variables within functions via the "global" keyword

global_variable_four = "Global variable four"


def modify_global_variable():
    global global_variable_four
    print(global_variable_four)

    global_variable_four = "New value for global variable four"
    print(global_variable_four)


modify_global_variable()
