'''
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
'''

a = 100
b = 200

if a > b:
  print("a is greater than b")
elif a == b:
  print("a and b are equal")
else:
  print("b is greater than a")

# Short Hand If
if b > a: print("b > a")

# Short Hand If ... Else
print("b > a") if(a > b) else print("a > b")

# One line if else statement, with 3 conditions:
a = 11
b = 11
print("a > b") if a > b else print("a == b") if a == b else print("a < b")

# and
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# or
if a > b or c > a:
    print("At least one of the conditions is True")

# if statements cannot be empty, but if you for some reason have an if statement with no content
# put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass

