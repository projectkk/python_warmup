# Kelly Fitzpatrick

# February 13, 2016
# Versions: python 3.5.1 | Anaconda 2.4.1


'''Because strings are immutible in python when passing
a string into a function only the value of the string is
passed. Therefore the origional string will remain unchanged.
'''
def change_string(string):
	string = string + " I like to party"
	print("String in function: ",string)

name = "Kelly"
print("String before passing: ",name)
change_string(name)
print("String after passing: ",name)

