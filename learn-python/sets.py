# Sets are collections of data
# They are a built-in data type in Python
# (just like lists, tuples and dictionaries)
# Sets are immutable (although items can be added or removed), unordered,
# have no indices and do not allow duplicate items
# Set items are immutable (unchangeable) and unordered but can be
# added or removed
# Because sets are unordered, the order cannot be predicted
# Duplicate items (items with the same values) are removed
# (e.g. {(1, 2), (1, 3)} works but {1, 1} is converted to {1})
# They can store any data type (strings, integers, booleans, etc.)

variable = {"Alice", 2, True, -2.3, True}  # The duplicate is removed
print(variable)
print(type(variable))

# Because sets have no indices, for loops are used to access all set items

for item in variable:
    print(item)

# The in keyword is used to check for a specific value within the set

print(-2.3 in variable)  # Prints True

# Return if two sets have no intersection via the isdisjoint() method
# (True if 0 identical items present in both sets, otherwise False)

variable = {1, 2}
variable_two = {3, 4}
print(variable.isdisjoint(variable_two))  # Prints True

variable = {1, 2}
variable_two = {2, 3}
print(variable.isdisjoint(variable_two))  # Prints False

# Return if another set contains this set

variable = {3, 2}
variable_two = {1, 2, 3, 4}
print(variable.issubset(variable_two))  # Prints True

variable = {1, 2}
variable_two = {2, 3, 4, 5}
print(variable.issubset(variable_two))  # Prints False

# Return if this set contains another set

variable = {1, 2, 3, 4}
variable_two = {3, 2}
print(variable.issuperset(variable_two))  # Prints True

variable = {2, 3, 4, 5}
variable_two = {1, 2}
print(variable.issuperset(variable_two))  # Prints False

# Individual items can be added via the add() method

variable = {"Alice", 2, True, -2.3, True}
variable.add("Bob")
print(variable)

variable.add(1)  # Does not add 1 because True already exists
print(variable)

# Items from other sets can be inserted via the update() method

variable_two = {False, 42}
variable.update(variable_two)
print(variable)

variable_three = {0}
variable.update(variable_three)  # Does not add 0 because False already exists
print(variable)

# This works for other iterables (lists, tuples, dictionaries, etc.) as well

variable = {1, "Alice", False}
variable_two = [3, 4, "Hello"]
variable.update(variable_two)
print(variable)

variable_three = (5, 6)
variable.update(variable_three)
print(variable)

variable_four = {"key1": "World", 2: "Charlie"}
variable.update(variable_four)  # Adds the keys, not the values
print(variable)

variable.update(variable_four.values())  # Adds the values, not the keys
print(variable)

variable.update(variable_four.items())  # Adds the items as tuples
print(variable)

# Alternatively, the union() method can be used
# Returns a new set rather than inserting items

variable = {1, 2, 3}
variable_two = {4, 5}
variable_three = variable.union(variable_two)
print(variable_three)

# Update a set by keeping only items present in both sets via the
# intersection_update() method

variable = {1, 2, 3, 4}
variable_two = {3, 4, 5}
variable.intersection_update(variable_two)  # Contains 3 and 4
print(variable)

# Return a new set containing only items present in both sets via
# the intersection() method

variable = {1, 2, 3, 4}
variable_two = {3, 4, 5}
variable_three = variable.intersection(variable_two)  # Contains 3 and 4
print(variable_three)

# Update a set by keeping only items not present in both sets via the
# symmetric_difference_update() method

variable = {1, 2, 3, 4}
variable_two = {3, 4, 5}
variable.symmetric_difference_update(variable_two)  # Contains 1, 2 and 5
print(variable)

# Return a new set containing only items not present in both sets via
# the symmetric_difference() method

variable = {1, 2, 3, 4}
variable_two = {3, 4, 5}
variable_three = variable.symmetric_difference(variable_two)
# Contains 1, 2 and 5
print(variable_three)

# Python usually references sets rather than copying them

original_set = {1, 2, 3}
set_copy = original_set
print(set_copy)

original_set.add(4)  # Also adds 4 to set_copy because it is a reference
print(original_set)
print(set_copy)

set_copy.add(5)  # Also adds 5 to original_set because it is a reference
print(original_set)
print(set_copy)

# The copy() method can be used to copy sets rather than referencing them

original_set = {1, 2, 3}
set_copy = original_set.copy()
print(set_copy)

original_set.add(4)  # Does not add 4 to set_copy because it is a copy
print(original_set)
print(set_copy)

set_copy.add(5)  # Does not add 5 to original_set because it is a copy
print(original_set)
print(set_copy)

# Items can be removed using the remove() method
# (raises an error if the item does not exist)

variable = {"Charlie", "Hello", -2, False, 3, 5}
variable.remove("Hello")
print(variable)

# Or via the discard() method
# (does not raise errors)

print(variable)
variable.discard(42)  # No error despite 42 not being an item
print(variable)

variable.discard("Charlie")
print(variable)

# The pop() method removes the last item
# This item will be random because sets are unordered

variable.pop()
print(variable)

# The len() function returns the length of a set (amount of items)

print(len(variable))

# The constructor function set() can be used to create a set
# (notice the two parenthesis)

variable = set((1, "Hello", False))
print(variable)
print(type(variable))

# Sets can be emptied via the clear() function

print(variable)
variable.clear()
print(variable)  # Prints set()

# Delete the set using the del keyword

del variable  # Interacting with sets after they are deleted will raise errors
