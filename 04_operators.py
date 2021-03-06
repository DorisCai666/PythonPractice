### Arithmetic operators are used with numeric values to perform common mathematical operations

x = 10
y = 3

# +	Addition
print(x + y)
# -	Subtraction
print(x - y)
# *	Multiplication
print(x * y)
# / Division
print(x / y)
# %	Modulus
print(x % y)
# ** Exponentiation
print(x ** y)
# // Floor division
print(x // y)

### Comparison operators are used to compare two values:

# ==	Equal
x == y
# !=	Not equal
x != y
# >	Greater than
x > y
# <	Less than
x < y
# >=	Greater than or equal to
x >= y
# <=	Less than or equal to
x <= y


### Logical operators are used to combine conditional statements:

# and 	Returns True if both statements are true
x < 5 and  x < 10
# or	Returns True if one of the statements is true
x < 5 or x < 4
# not	Reverse the result, returns False if the result is true
not(x < 5 and x < 10)


### Identity operators are used to compare the objects,
### not if they are equal, but if they are actually the same object, with the same memory location:

# is 	  Returns true if both variables are the same object
x is y
# is not	 Returns true if both variables are not the same object
x is not y


### Membership operators are used to test if a sequence is presented in an object:

# in 	Returns True if a sequence with the specified value is present in the object
x = "a"
y = "abc"
x in y
# not in	Returns True if a sequence with the specified value is not present in the object
x not in y

### Bitwise operators are used to compare (binary) numbers

# & 	AND	Sets each bit to 1 if both bits are 1
# |	    OR	Sets each bit to 1 if one of two bits is 1
# ^	    XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


### Assignment operators are used to assign values to variables

# =
x = 5
# +=
x += 3
x = x + 3
# -=
x -= 3
x = x - 3
# *=
x *= 3
x = x * 3
# /=
x /= 3
x = x / 3
# %=
x %= 3
x = x % 3
# //=
x //= 3
x = x // 3
# **=
x **= 3
x = x ** 3
# &=
x = 5
x &= 3
x = x & 3
# |=
x |= 3
x = x | 3
# ^=
x ^= 3
x = x ^ 3
# >>=
x >>= 3
x = x >> 3
# <<=
x <<= 3
x = x << 3