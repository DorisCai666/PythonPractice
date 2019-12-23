
# Assign String to a Variable
x = "Hey, Doris"
print(x)

# Get the character at position (remember that the first character has the position 0):
print(x[2:5])
print(x[-1])
print(x[0:-4])

# You can assign a multi line string to a variable by using three quotes:
a = """You may say that I'm a dreamer,
But I'm not the only one."""
print(a)

a = ''' 
Let it be, 
let it be, 
let it be, 
let it be 
'''
print(a)

# Casting in python is therefore done using constructor functions:
x = str("Hello World")
print(x)

a = " Hello, World! "

# The len() function returns the length of a string
print(len(a))

# The strip() method removes any whitespace from the beginning or the end
print(a.strip())

# The upper() method returns the string in upper case
print(a.upper())

# The lower() method returns the string in lower case
print(a.lower())

# The replace() method replaces a string with another string
print(a.replace("Hello", "Hi"))

# The split() method splits the string into substrings if it finds instances of the separator
print(a.split(","))

# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
x = "ain" not in txt
print(x)

# Merge variable a with variable b into variable c
a = "a and b "
b = "together now"
c = a + b
print(c)

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
a = "have"
b = 3
c = "cats"
strorder = "I {} {} lovely {} at home."
print(strorder.format(a, b, c))

# An escape character is a backslash \ followed by the character you want to insert.

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
