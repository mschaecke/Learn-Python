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
# Agree upon a naming convention in group projects (often snake case)

name = "Hello"
Name = "World"

print(name)
print(Name)

othervariable = 1  # A separator for multiple words is preferred
otherVariable = 2  # This is known as camel case
other_variable = 3  # A common naming convention in Python is snake case
_other_Variable = 4
OtherVariable = 5  # This is known as pascal case
OTHERVARIABLE = 6

# Assign different values to multiple variables in a single line

var_one, var_two, var_three = 1, 2, 3

print(var_one)
print(var_two)
print(var_three)

# Assign the same value to multiple variables in a single line

var_one = var_two = var_three = 1

print(var_one)
print(var_two)
print(var_three)

# This can be used to swap the values of multiple variables as well

a, b, c = 1, 2, 3

print(a, b, c)

a, b, c = c, a, b

print(a, b, c)

# Unpack a collection of values (list, tuple, etc.)
# The values are extracted and assigned to variables

# This works for lists

names = ["Alice", "Bob", "Charlie"]
name_one, name_two, name_three = names

print(name_one)
print(name_two)
print(name_three)

# tuples,

numbers = (1, 2, 3)
number_one, number_two, number_three = numbers

print(number_one)
print(number_two)
print(number_three)

# strings,

string = "Abc"
string_one, string_two, string_three = string

print(string_one)
print(string_two)
print(string_three)

# dictionaries

dictionary = {"A": 1, "B": 2}
key_one, key_two = dictionary  # assign the keys

print(key_one)
print(key_two)

value_one, value_two = dictionary.values()  # assign the values

print(value_one)
print(value_two)

item_one, item_two = dictionary.items()  # assign the items as tuples

print(item_one)
print(item_two)

# and coordinates (which in this case are a list of floats)

coordinates = [1.467, 3.653]
x, y = coordinates

print(x, y)

# Values can be ignored via "_"

value_one, _, value_three = (1, 2, 3)

print(value_one)
print(value_three)

# and multiple values can be assigned to one variable via "*"

value_one, *value_two, value_three = (1, 2, 3, 4, 5)

print(value_one)
print(value_two)  # Output = [2, 3, 4]
print(value_three)

# Both can be combined as well

*_, value_two, value_three = (1, 2, 3, 4, 5)

print(value_two)  # Output = 4
print(value_three)  # Output = 5

# Use print() to output a single variable

var_one = 1

print(var_one)

# Use print() to output multiple variables

var_one, var_two, var_three = "How", "are", "you?"

print(var_one, var_two, var_three)

# The "+" operator can be used as well (notice the lack of spaces)

print(var_one + var_two + var_three)

# This does NOT work for numbers because "+" is a mathematical operator
# (addition) in this case

var_one, var_two, var_three = 1, 2, 3

print(var_one + var_two + var_three)

# If both a number (e.g. 1) and string (e.g. "Hello") are printed via "+"
# operator, an error occurs
# Use ","  to output multiple variables, especially of different data types

var_one, var_two = 1, "Hello"

print(var_one, var_two)

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
