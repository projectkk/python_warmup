# Kelly Fitzpatrick

# February 13, 2016
# python 3.5.1 | Anaconda 2.4.1

""" This is an intro to strings in python. Creating string variables,
printing, and using string functions.
"""

var1 = "flowers"
var2 = 'chocolate'
var3 = "jewlery"
var4 = "I like "

print('\n',var1, var2, var3, var4, '\n')

# Concatenate two strings
var5 = var4 + var1
print(var5)

# Repeat two strings
print(var5*2)

# Access a single character, zero based
print(var1[0])

# Access a slice of a string, zero based
print(var1[0:3])

# Will return true if character/s in string
print('co' in var2)
print('cp' in var2)

# Will return true if character/s not in string
print('co'not in var2)
print('cp'not in var2)

# r & R allow you to print Escape characters
print('\n return', r'\t tab', R'\n return',var3)

""" Useful string functions """

# Capitalize first letter of a string
print(var1.capitalize())

# Counts how many times str occurs in string or in a substring
print(var2.count('c'))
print(var2.count('c',1,len(var2)))

# Determines if string or a substring ends with a suffix, returns true/false
print(var3.endswith('ry'))
print(var3.endswith('ry', 2, len(var3)))
print(var3.endswith('rw'))

# Determines if str occurs in string or substring and return the index
# returns -1 if not found
print(var3.find('ew'))
print(var3.find('ew', 0, 4))
print(var3.find('o'))
