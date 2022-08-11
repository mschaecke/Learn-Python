# Strings (str) are used for text including single characters
# Single (' '), double (" ") or triple quotes (''' ''' or """ """)
# can be used for string variables

variable = 'This is a string variable'
print(variable)
print(type(variable))

variable = "This is also a string variable"
print(variable)

variable = '''
This is
a multiline
string variable
'''
print(variable)

# Multiline strings may even include line breaks

variable = """
This is also 

a multiline 

string variable
"""
print(variable)

# String constructor function
# Converts various data types (e.g. string, integer, float) to string

# This example shows string to string

variable = str("This is a string specified via the constructor function")
print(variable)
print(type(variable))

# This example shows integer to string

variable = str(2)
print(variable)
print(type(variable))

# This example shows float to string

variable = str(2.3)
print(variable)
print(type(variable))

# Strings are arrays of characters
# Individual characters are strings with a length of 1

# The len() function can be used to get the length of a string

variable = "Hello"
print(len(variable))  # Output = 5

# String elements can be accessed via [] just like array elements

variable = "World"
print(variable[4])  # Output = "d" because arrays start at position 0

# Ranges of a string can be accessed using [] (referred to as slicing)
# The start and end index are specified within the []
# The end index is excluded

variable = "abcde"

print(variable[1:3])  # Output = "bc" (notice the exclusion of "d")

print(variable[:4])  # Output = "abcd" by removing the start index

print(variable[3:])  # Output = "de" by removing the end index

# Negative values can be utilized to start from the end of a string
# Counting starts at 1 (instead of 0) in this case
# The end index is excluded again

variable = "abcde"

print(variable[-4:-2])  # Output = "bc" (notice the exclusion of "d")

print(variable[:-3])  # Output = "ab"

print(variable[-2:])  # Output = "de"

# Check if the string contains a character or string via "in"

variable = "How are you?"

if "are" in variable:  # "in" can be used without the "if"
    print('The string contains the word "are".')

# Check if it is not contained in the string via "not in"

variable = "How are you?"

if "Hello World!" not in variable:  # "not in" can be used without the "if"
    print('"Hello World!" is not present in the string')

# Loops can be used as well

variable = "abcd"

for character in variable:
    print(character)

# Python offers various string functions
# They return new values but do not change the original string
# A few examples are:

# Count the amount of times a value occurs within the string

variable = "Hello World! Hello World! Hello World!"
print(variable.count("Hello"))  # Output = 3

# Identify the position of a value within the string

variable = "Hello World!"
print(variable.find("orl"))  # Output = 7

# Check if all characters are alphanumeric
# (alphabetical and numerical characters)

variable = "Hello123"
print(variable.isalnum())  # Output = True

# Check if all characters are in the alphabet

variable = "Hello123"
print(variable.isalpha())  # Output = False

# Check if all characters are decimals (0-9)

variable = "42"
print(variable.isdecimal())  # Output = True

variable = "42.123"
print(variable.isdecimal())  # Output = False

# Check if all characters are digits (includes exponents)

variable = "2\u00B2"
print(variable)  # Output = "2²"
print(variable.isdigit())  # Output = True

# Check if all characters are numeric
# (numeric (0-9), includes exponents, excludes "-" and ".")

variable = "-42"
print(variable.isnumeric())  # Output = False

# Check if the string is an identifier
# (alphanumeric or underscores, no spaces, does not start with a number)

variable = "identifier_123"
print(variable.isidentifier())  # Output = True

variable = "123_identifier"
print(variable.isidentifier())  # Output = False

# Check if all characters are whitespaces

variable = "   "
print(variable.isspace())  # Output = True

# Replace parts of a string

variable = "How"
print(variable)

print(variable.replace("H", "N"))  # Output = "Now"

# Lower case of a string

variable = "HELLO!"
print(variable.lower())

# Check if a string is lower case

variable = "hello"
print(variable.islower())  # Output = True

# Upper case of a string

variable = "world!"
print(variable.upper())

# Check if a string is upper case

variable = "World!"
print(variable.isupper())  # Output = False

# Capitalize the first character

variable = "hello"
print(variable.capitalize())

# Capitalize the first character of each word

variable = "how are you?"
print(variable.title())  # Output = "How Are You?"

# Swap lower and upper case

variable = "Hello World!"
print(variable.swapcase())  # Output = "hELLO wORLD!"

# Remove whitespaces from the beginning and end of a string
# Works for "\n" (new line), "\t" (horizontal tab) and "\v" (vertical tab) too

variable = " How are you? "
print(variable.strip())

# Join all items in an iterable (e.g. tuple, dictionary) into a string
# utilizing the specified separator

tuple_one = ("Hello", "World", "!")
separator = "_"

print(separator.join(tuple_one))  # Output = "Hello_World_!"

dictionary_one = {"name": "Bob", "age": "20"}
print("+".join(dictionary_one))  # "+" is the separator
# Output = "name+age", the keys (not values) are returned

print("+".join(dictionary_one.values()))
# Output = "Bob+20", the values (not keys) are returned

# Split the string into substrings by specifying a separator
# (Output = list containing list items excluding the separator)

variable = "This, is, a string!"
print(variable.split(","))  # Output = ['This', ' is', ' a string!']

# Concatenate (combine) multiple strings via the "+" operator

variable = "World!"
print("Hello " + variable)

variable = "How "
variable_two = "are you?"

variable_three = "Hello World!" + " " + variable + variable_two
print(variable_three)

# Strings can be created via "f-string"
# This is especially useful for multiple variables,

variable, variable_two = 2, "is"

print(f"{variable} plus {variable} {variable_two} 4")

# multiple expressions,

variable = "Hello "
print(f"{variable}" * 5)

print(f"{variable * 5}")

# mathematical calculations,

result = f"{2 * 3 ** 2}"
print(result)

# value conversions

variable = 42
print(f"The value is {float(variable)}.")

# or lists

print(f"{[1, 2, 3, 4]}")

# "F" or single quotes work too

variable = "Hello"
print(F'{variable} World')

# Triple quotes are possible

variable_two = "is"
variable_three = "multiline"

print(f"""
{variable} World!
This {variable_two}
a {variable_three}
string variable
""")

# Newer versions of Python (3.6 and later) utilize "f-string" as shown above
# Older versions of Python (earlier than 3.6) use the format() method
# It accepts an unlimited amount of arguments, formats them and replaces the
# placeholders {} within the string
# Placeholders can be specified via name or index within the formatted string

variable = "Hello {}! 2 * 2 = {}"
variable_two = "World"
variable_three = 4

print(variable.format(variable_two, variable_three, variable))
# (notice the last argument (variable) is not printed because there are only
# two placeholders)

# Certain characters can only be used within strings by
# utilizing escape characters
# They are indicated by a backslash \ and the specific characters

# The following escape characters exist:

#   \newline        Ignored
#   \\              Backslash (\) (inserts one \ into a string)
#   \'              Single quote (‘) (useful within single quote strings)
#   \"              Double quote (“) (useful within double quote strings)
#   \a              ASCII Bell (BEL)
#   \b              ASCII Backspace (BS) (erases one character within a string)
#   \f              ASCII Form feed (FF) (continue at the top of a new page)
#   \n              ASCII Line feed (LF) (creates a new line within a string)
#   \N{name}        Character named NAME in the Unicode database (Unicode only)
#   \r              ASCII Carriage Return (CR)
#   \t              ASCII Horizontal Tab (TAB) (creates a tab within a string)
#   \uxxxx          Character with 16-bit hex value XXXX (Unicode only)
#   \Uxxxxxxxx      Character with 32-bit hex value XXXXXXXX (Unicode only)
#   \v              ASCII Vertical Tab (VT)
#   \ooo            Character with octal value OOO (e.g. \110 for "H")
#   \xhh            Character with hex value HH (e.g. \x48 for "H")

# https://python-reference.readthedocs.io/en/latest/docs/str/escapes.html
