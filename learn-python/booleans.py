# Booleans are either True or False
# They are especially useful when evaluating expressions containing
# comparison, identity or membership operators (<, >, ==, !=, is, in, etc.)
# True != true and False != false because Python is case-sensitive

variable = True
print(variable)
print(type(variable))  # Output = <class 'bool'>

variable = 5 > 7  # variable = False
print(variable)
print(type(variable))

# This is also useful for if statements

age = 30

if age >= 18:
    print("You can vote.")  # This will be printed
else:
    print("You are too young to vote.")

name = "Peter"
group_members = ["Alice", "Bob", "Charlie"]

if name in group_members:
    print("You are a group member.")
else:
    print("You are not a group member.")  # This will be printed

# The constructor function bool() can be used for evaluation
# Empty strings are False, all other strings are True
# 0 is False, all other numbers are True
# Empty lists, tuples, dictionaries and sets are False, all other ones are True
# In general empty values like "", [], etc. (can often be evaluated via
# the len() function), the number 0 and None are False
# All other values are True

print(bool(True))  # Output = True
print(bool(False))  # Output = False
print(bool(None))  # Output = False

print(bool(""))  # Output = False
print(bool("Hello"))  # Output = True
variable = ""
print(bool(len(variable)))  # Output = False
variable = "Hello"
print(bool(len(variable)))  # Output = True

print(bool(0))  # Output = False
print(bool(42))  # Output = True
print(bool(-42.89))  # Output = True

print(bool([]))  # Output = False
print(bool(["Alice", "Bob", "Charlie"]))  # Output = True
print(bool(()))  # Output = False
print(bool((1, 2, 3)))  # Output = True

# Some functions return a boolean value

variable = "hello".isupper()  # variable = False
print(variable)

variable = "hello".islower()  # variable = True
print(variable)

variable = 42.89
print(isinstance(variable, float))  # Prints True

# The following operators return boolean values
# They can be used with various data types (booleans, strings, integers, etc.)

# Comparison operators compare two values

# Equality (equal) "=="

variable = 1 == 1
print(variable)
print(type(variable))

variable = "Hello" == "World"
print(variable)
print(type(variable))

# Negated equality (not equal) "!="

variable = 1 != 1  # variable = False
print(variable)
print(type(variable))

variable = 1 != 2  # variable = True
print(variable)
print(type(variable))

# Greater than ">"

variable = 2 > 1
print(variable)
print(type(variable))

variable = "a" > "b"  # variable = False
print(variable)
print(type(variable))

# Less than "<"

variable = 1 < 2
print(variable)
print(type(variable))

variable = "a" < "b"  # variable = True
print(variable)
print(type(variable))

# Greater than or equal ">="

variable = 2 >= 1
print(variable)
print(type(variable))

variable = "a" >= "b"  # variable = False
print(variable)
print(type(variable))

# Less than or equal "<="

variable = 1 <= 2
print(variable)
print(type(variable))

variable = "a" <= "b"  # variable = True
print(variable)
print(type(variable))

# Logical operators combine conditional statements or negate them

# "and" operator
# Returns True if both statements are True, returns False otherwise

variable = True and True  # variable = True
print(variable)
print(type(variable))

variable = True and False  # variable = False
print(variable)
print(type(variable))

variable = False and False  # variable = False
print(variable)
print(type(variable))

variable = 1 == 1 and "Hello" == "Hello"  # variable = True
print(variable)
print(type(variable))

variable = 1 > 1 and "Hello" == "Hello"  # variable = False
print(variable)
print(type(variable))

# "or" operator
# Returns True if one or both statements are True, returns False otherwise

variable = True or True  # variable = True
print(variable)
print(type(variable))

variable = True or False  # variable = True
print(variable)
print(type(variable))

variable = False or False  # variable = False
print(variable)
print(type(variable))

variable = 1 == 1 or "Hello" == "Hello"  # variable = True
print(variable)
print(type(variable))

variable = 1 > 1 or "Hello" == "Hello"  # variable = True
print(variable)
print(type(variable))

variable = 1 > 1 or "Hello" != "Hello"  # variable = False
print(variable)
print(type(variable))

# "not" operator
# Negates the result

variable = not True  # variable = False
print(variable)
print(type(variable))

variable = not False  # variable = True
print(variable)
print(type(variable))

variable = not (True and True)  # variable = False
print(variable)
print(type(variable))

variable = not (True and False)  # variable = True
print(variable)
print(type(variable))

variable = not (True or False)  # variable = False
print(variable)
print(type(variable))

variable = not (False or False)  # variable = True
print(variable)
print(type(variable))

variable = not True and True  # variable = False
print(variable)
print(type(variable))

variable = not False and True  # variable = True
print(variable)
print(type(variable))

variable = not False or False  # variable = True
print(variable)
print(type(variable))

# The identity operators "is" and "is not" compare two objects regarding their
# identity ("Are the two objects the same object?" or "Do they have the same
# memory locations?", not "Are they equal (==)?")

# "is" operator
# Returns True if both objects are the same object, returns False otherwise

object_one = [1, 2, 3]
object_two = object_one
object_three = [1, 2, 3]  # [1, 2, 3] is a new object with the same content

variable = object_one is object_two  # variable = True
print(variable)
print(type(variable))

variable = object_one is object_three  # variable = False
print(variable)
print(type(variable))

# "is not" operator
# Returns True if both objects are not the same object, returns False otherwise

object_one = [1, 2, 3]
object_two = object_one
object_three = [1, 2, 3]  # [1, 2, 3] is a new object with the same content

variable = object_one is not object_two  # variable = False
print(variable)
print(type(variable))

variable = object_one is not object_three  # variable = True
print(variable)
print(type(variable))

# Membership operators test if a value contains the specified sequence

# "in" operator
# Returns True if the object contains the sequence, returns False otherwise

object_one = "Hello"
sequence = "ell"
variable = sequence in object_one  # variable = True
print(variable)
print(type(variable))

object_one = [1, 2, 3]
sequence = 4
variable = sequence in object_one  # variable = False
print(variable)
print(type(variable))

# "not in" operator
# Returns True if the object does not contain the sequence, returns
# False otherwise

object_one = "Hello"
sequence = "ell"
variable = sequence not in object_one  # variable = False
print(variable)
print(type(variable))

object_one = [1, 2, 3]
sequence = 4
variable = sequence not in object_one  # variable = True
print(variable)
print(type(variable))

# Python also offers bitwise operators (&, |, ^, ~, <<, >>) to
# compare binary numbers
# The topic is more advanced and therefore not relevant for this introduction

# # Operator precedence
# # Upper groups have a higher precedence than lower ones
# # The empty line separates groups of operators with the same precedence

# Brackets / Parentheses
# ()

# Mathematical operators
# **, *, /, //, %, +, -

# Bitwise operators
# &, |, ^, ~, <<, >>

# Comparisons, identity and membership operators
# ==, !=, >, >=, <, <=, is, is not, in, not in

# Logical "not"
# not

# Logical "and"
# and

# Logical "or"
# or

# https://docs.python.org/3/reference/expressions.html#operator-precedence

# If the operators have the same precedence, the associativity is left-to-right

variable = True or False or True  # variable = True
print(variable)
print(type(variable))

# A few examples:

variable = 1 == 1 and "Hello" == "Hello"  # variable = True
print(variable)
print(type(variable))

variable = not True and 2 > 1  # variable = False
print(variable)
print(type(variable))

variable = True and (1 > 2 or not False)  # variable = True
print(variable)
print(type(variable))

names = ["Alice", "Bob", "Charlie"]

if "Bob" in names and False or 1 == 1:
    print("The if statement is True ")  # This is printed
else:
    print("The if statement is False")
