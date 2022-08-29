# Lists are collections of data
# They are a built-in data type in Python (just like tuples, sets and
# dictionaries) and work similar to arrays in other programming languages
# Lists are mutable (both the order and individual items can be changed),
# ordered and allow duplicate items
# They can store any data type (strings, integers, booleans, etc.)

variable = [1, 2, 3]
print(variable)
print(type(variable))  # Prints object of data type list

# Unlike arrays in other programming languages, lists can store multiple
# data types at once

variable = ["Alice", 2, True]
print(variable)
print(type(variable))

# They can store other lists

variable = [1, [2, 3, 4], 5, [[6, 7], [8, 9, 0]]]
print(variable)
print(type(variable))

# Individual items can be accessed via the index and []
# The index starts at 0 and ends at len() - 1
# Negative index values work as well

variable = ["Alice", "Bob", "Charlie"]
print(variable[1])  # Prints "Bob"
print(variable[-1])  # Prints "Charlie"

# Strings are very similar to lists
# They can be considered an ordered collection of individual characters
# (length of 1)

variable = "Alice"
print(variable[3])  # Prints "c"
print(variable[-1])  # Prints "e"

# Lists within lists can be accessed via [][]

variable = [[1, 2], [3, 4]]
print(variable[1][0])  # Prints 3

# Multiple values can be returned as a list by specifying a range of indices
# (start and end) and optionally a step value
# The value at the end index is excluded

variable = [1, 2, 3, 4, 5, 6]
variable_two = variable[1:4]  # variable_two = [2, 3, 4]
print(variable_two)

variable_two = variable[2:]  # variable_two = [3, 4, 5, 6]
print(variable_two)

variable_two = variable[:3]  # variable_two = [1, 2, 3]
print(variable_two)

# Negative values can be used

variable_two = variable[-4:-2]  # variable_two = [3, 4]
print(variable_two)

# A step value can be specified too

variable_two = variable[::2]  # variable_two = [1, 3, 5]
print(variable_two)

variable_two = variable[1::2]  # variable_two = [2, 4, 6]
print(variable_two)

variable_two = variable[:4:3]  # variable_two = [1, 4]
print(variable_two)

# List items can be accessed using loops

variable = [1, 2, 3, 4, 5]

# For loop

for value in variable:
    print(value)

# For loop with range()

for i in range(2):
    print(variable[i])  # Prints 1 and 2

# For loop with range() and len()

for i in range(len(variable)):
    print(variable[i])

# While loop

i = 0
while i < len(variable):
    print(variable[i])
    i += 1

# List comprehension (will be explained in more detail later)

[print(value) for value in variable]

# Reverse a list using reverse()

variable = [1, 2, 3, 4, 5]
variable.reverse()
print(variable)

# Reverse the list via -1 step value

variable = [1, 2, 3, 4, 5]
variable_two = variable[::-1]  # variable_two = [5, 4, 3, 2, 1]
print(variable_two)

# The length of a list (amount of items) can be returned via the len() function
# (similar to strings)

variable = [1, 2, 3]
print(len(variable))  # Prints 3

variable = "Bob"
print(len(variable))  # Prints 3

# The existence of an item in a list can be determined via the in keyword

variable = [1, 2, 3, 4]
print(2 in variable)  # Prints True

variable = ["Alice", "Bob"]
print("Charlie" in variable)  # Prints False

# Items can be added, modified and removed

variable = ["Alice", 2, 3, True, [2, 3]]
print(variable)

variable.append(4)  # Adds 4 at the end of the list
print(variable)

variable[0] = "Bob"  # Changes "Alice" to "Bob
print(variable)

variable.remove(True)  # Removes True
print(variable)

variable.append(4)  # Adds another 4 at the end of the list
print(variable)

variable.insert(3, "Hello")  # Inserts a new value instead of changing it
print(variable)  # Output = ['Bob', 2, 3, 'Hello', [2, 3], 4, 4]

variable.insert(4, [True, False])  # Inserts a list instead of changing it
print(variable)  # Output = ['Bob', 2, 3, 'Hello', [True, False], [2, 3], 4, 4]

variable = [1, 2, 3]
variable_two = [4, 5]
variable.extend(variable_two)  # Add the second list to the end of the first
print(variable)  # Output = [1, 2, 3, 4, 5]

variable = [1, 2, 3]
variable_two = (4, 5)  # This works with all iterables like tuples
variable_three = {6: "Hello", 7: "World"}  # or dictionaries
variable.extend(variable_two)
print(variable)  # Output = [1, 2, 3, 4, 5]
variable.extend(variable_three)
print(variable)  # Output = [1, 2, 3, 4, 5, 6, 7]

# Multiple values can be changed using a specified range

variable = [1, 2, 3, 4, 5]
print(variable)
variable[2:4] = [6, 7]  # variable = [1, 2, 6, 7, 5]
print(variable)

more_values = [23, 34, 45, 56, 67, 78, 89]
variable[1:3] = more_values  # variable = [1, 23, 34, 45, 56, 67, 78, 89, 7, 5]
print(variable)
print(len(variable))  # Output = 10

less_values = [42]
variable[2:] = less_values  # Replaces all values after index 1 (including 2)
print(variable)
print(len(variable))  # Output = 3

variable[:2] = [0, 9, 8, 7, 6]  # Replaces all values before index 2
print(variable)
print(len(variable))  # Output = 6

# There are multiple ways to remove items

variable = [1, 2, 3, 4, 5]
print(variable)

variable.remove(4)  # Removes the specified item
print(variable)

variable.pop()  # Removes the last item
print(variable)

variable.pop(1)  # Removes item at the specified index
print(variable)

del variable[0]  # Removes item at the specified index as well
print(variable)

# The entire list can be cleared or deleted

variable = [1, 2, 3]
print(variable)
variable.clear()  # variable = []
print(variable)

del variable  # variable is completely deleted

# Lists can be sorted in various ways

variable = [2, 3, 5, 4, 2, 42, 89, 0]
print(variable)
variable.sort()
print(variable)

variable = ["Charlie", "Alice", "Bob"]
print(variable)
variable.sort()
print(variable)

# Sort is case-sensitive (upper before lower case)

variable = ["a", "A", "b", "C", "c"]
print(variable)
variable.sort()
print(variable)  # Prints ['A', 'C', 'a', 'b', 'c']

# Sort can be case-insensitive using key=str.lower

variable = ["c", "A", "a", "C", "b"]
print(variable)
variable.sort(key=str.lower)
print(variable)  # Prints ['A', 'a', 'b', 'c', 'C']

# A descending order is possible as well

variable = [2, 3, 5, 4, 2, 42, 89, 0]
print(variable)
variable.sort(reverse=True)
print(variable)

variable = ["Charlie", "Alice", "Bob"]
print(variable)
variable.sort(reverse=True)
print(variable)


# Sort using a custom function
def even(x):
    return x % 2 == 0


variable = [1, 2, 3, 4, 5]
variable.sort(key=even)
print(variable)  # Prints [1, 3, 5, 2, 4]

variable = [1, 2, 3, 4, 5]
variable.sort(key=even, reverse=True)
print(variable)  # Prints [2, 4, 1, 3, 5]

# TODO: Other list methods

# The constructor function list() can be used to create a list as well
# (unlike the [] notion, the function uses two parenthesis)

variable = list((1, 2, "Hello", "World", False))
print(variable)
print(type(variable))

# List comprehension
# Uses the following syntax:
# variable_name = [expression for item in iterable]
# Expressions can be the current item or manipulations of the item
# (e.g. print(x), x.lower() or x * 2)
# Iterables are objects like lists, tuples, sets, etc.
# Additionally, one or multiple conditions can be added (condition must be met)
# variable_name = [expression for item in iterable if condition == True]

# A simple list containing the numbers 0 to 9
# Can be used instead of for loops

variable = [value for value in range(10)]
print(variable)

# Only even numbers (0, 2, 4, 6 and 8 in this case)

variable = [value for value in range(10) if value % 2 == 0]
print(variable)

# Only even numbers using the even() function

variable = [value for value in range(10) if even(value)]
print(variable)

# Only even numbers > 5 (6 and 8 in this case)

variable = [value for value in range(10) if value % 2 == 0 and value > 5]
print(variable)

# Print odd numbers separately

[print(value) for value in range(10) if value % 2 == 1]

# Create a new list based on an existing list

variable = [value for value in range(10)]
new_variable = [x * 2 for x in variable]
print(new_variable)

variable = ["Alice", "Bob", "Charlie"]

new_variable = [names for names in variable if "i" in names]
print(new_variable)

variable = [x for x in range(5)]
new_variable = ["x" for item in variable]  # "x" instead of the number
print(new_variable)

variable = [x for x in range(10)]
# Return True if item is even,
# else return False
# as new list called new_variable
new_variable = [True if x % 2 == 0 else False for x in variable]
print(new_variable)
