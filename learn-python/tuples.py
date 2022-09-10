# Tuples are collections of data
# They are a built-in data type in Python
# (just like lists, sets and dictionaries)
# Tuples are immutable (unchangeable), ordered and allow duplicate items
# Tuple items are immutable (unchangeable), ordered and allow duplicate values
# Because they are immutable (no adding, modifying or removing items),
# the order does not change after the tuple is created
# They can store any data type (strings, integers, booleans, etc.)

variable = ("Alice", 1, True, -2.3, True)
# Assigning values is also called packing a tuple
print(variable)
print(type(variable))

# Creating a tuple with one item requires a comma after the item

tuple_one = (True,)
print(tuple_one)
print(type(tuple_one))  # Prints <class 'tuple'>

# Otherwise it will be treated as regular parentheses by Python

tuple_one = (True)  # IDEs will give the warning "redundant parentheses"
print(tuple_one)
print(type(tuple_one))  # Prints <class 'bool'>

# Values can be accessed and assigned to other variables
# This is also called unpacking a tuple
# The amount of variables and tuple items should be equal
# Otherwise * can be used to assign the remaining values as a list

coordinates = (42, 36, -50)

x, y, z = coordinates
print(x, y, z)  # Prints 42 36 -50

(x, y, z) = coordinates  # This works too
print(x, y, z)  # Prints 42 36 -50 as well

x, *other = coordinates
print(x, other)  # Prints 42 [36, -50]

*other, z = coordinates
print(other, z)  # Prints [42, 36] -50

number_tuple = (1, 2, 3, 4, 5)
x, *y, z = number_tuple
print(x, y, z)  # Prints 1 [2, 3, 4] 5

# Individual tuple items can be accessed via indices (starting at 0) and []

print(variable)  # Prints ('Alice', 1, True, -2.3, True)
print(variable[0])  # Prints "Alice"

# Negative indices work as well (-1 is the last item)

print(variable[-2])  # Prints -2.3

# Multiple items can be returned as a new tuple by specifying a range
# Notice the end of the range ([start:end]) will be excluded

print(variable[:2])  # Prints ('Alice', 1)
print(variable[3:])  # Prints (-2.3, True)
print(variable[2:4])  # Prints (True, -2.3)

# If the range is out of bounds, all available items are returned

print(variable[-1000:4])  # Prints ('Alice', 1, True, -2.3)
print(variable[2:1000])  # Prints (True, -2.3, True)

# Negatives values for ranges are possible

print(variable[-4:-2])  # Prints (1, True)

# The len() function returns the length of a tuple (amount of items)

print(len(variable))  # Prints 5

# Both for and while loops work with tuples

for value in variable:
    print(value)  # Prints the values individually

for index in range(len(variable)):  # Not recommended to access the index
    print(variable[index])

for i, value in enumerate(variable):  # Better version of range(len())
    print(i, value)

i = 0
while i < len(variable):  # The for loop shown above is preferred in this case
    print(variable[i])
    i += 1

# Check if an item exists in a tuple via the in keyword

if -2.3 in variable:
    print("-2.3 exists in the tuple")
else:
    print("-2.3 does not exist in the tuple")

# Count the amount of a specific element within the tuple via count()

print(variable)  # Prints ('Alice', 1, True, -2.3, True)
print(variable.count("Alice"))  # Prints 1

# Return the index of the first occurrence of a specific element within the
# tuple via index() method

print(variable)  # Prints ('Alice', 1, True, -2.3, True)
print(variable.index(-2.3))  # Prints 3

# Tuples can be concatenated via the + operator

variable = (1, 2, 3)
variable_two = (4,)

variable += variable_two
print(variable)  # Prints (1, 2, 3, 4)

# The * operator can be used to multiply tuples (not the values)

variable = variable * 2
print(variable)  # Prints (1, 2, 3, 4, 1, 2, 3, 4)

# It is possible to add, modify or delete items by
# converting tuples to lists, making the desired changes
# and converting the lists back to a tuples
# This is only a workaround and usually not recommended

variable = ("Alice", "Bob", "Charlie")
print(variable)
print(type(variable))

variable = list(variable)
print(variable)  # Prints ['Alice', 'Bob', 'Charlie']
print(type(variable))

variable.append(True)
print(variable)  # Prints ['Alice', 'Bob', 'Charlie', True]

variable[2] = 42
print(variable)  # Prints ['Alice', 'Bob', 42, True]

variable.pop()
print(variable)  # Prints ['Alice', 'Bob', 42]

variable.pop(1)
print(variable)  # Prints ['Alice', 42]

variable.remove("Alice")
print(variable)  # Prints [42]

variable = tuple(variable)
print(variable)  # Prints (42,)
print(type(variable))

# The constructor function tuple() can be used to create a tuple
# (notice the two parenthesis)

variable = tuple((1, 2, "Bob", False))
print(variable)
print(type(variable))

# Delete the tuple via the del keyword

del variable  # Interacting with tuples after they are deleted will raise errors
