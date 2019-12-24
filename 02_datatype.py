"""
Setting the Data Type
In Python, the data type is set when you assign a value to a variable:
"""

# str
x = "Hello World"
print(x)
x = str("Hello World")
print(x)

# int
x = 20
print(x)
x = int(x)
print(x)

# Python also has many built-in functions that returns a boolean value,
# like the isinstance() function, which can be used to determine if an object is of a certain data type
x = "aaa"
print(isinstance(x, int))
x = 101
print(isinstance(x, int))

# float
x = 20.5
print(x)
x = float(x)
print(x)

# Float can also be scientific numbers with an "e" to indicate the power of 10
x = 12e3
print(x)
x = 12E4
print(x)

# complex
# Complex numbers are written with a "j" as the imaginary part
x = 1j
print(x)
x = complex(2)
print(x)

# list
x = ["aa", "bb", "cc"]
print(x)
x = list(("aa", "bb", "cc"))
print(x)

# tuple
x = ("aa", "bb", "cc")
print(x)
x = tuple(("aa", "bb", "cc"))
print(x)

# range
x = range(6)
print(x)

#dict
x = {"name": "John", "age": 36}
print(x)
x = dict(name="John", age=36)
print(x)

#set
x = {"apple", "banana", "cherry"}
print(x)
x = set(("apple", "banana", "cherry"))
print(x)

# forzenset
x = frozenset({"apple", "banana", "cherry"})
print(x)

# bool
x = True
print(x)
x = bool(5)
print(x)

# bytes
x = b"Hello"
print(x)
x = bytes(5)
print(x)

# bytearray
x = bytearray(5)
print(x)

# memoryview
x = memoryview(bytes(5))
print(x)



