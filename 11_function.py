# Creating a Function
# In Python a function is defined using the def keyword

def first():
    print("first function")

# call a function
first()

# arguments
def bbking(name):
    print("The BBKing is s%", name)

bbking("Zhan Qingyun")
bbking("Qiu Chen")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.

def function_a(*students):
  print("The youngest student is " + students[2])

function_a("YY", "RR", "CC")

def function_b(student1,student2, student3):
    print("The youngest student is " + student3)

function_b(student1="YY", student2="CC", student3="RR")


# Default Parameter Value
# The following example shows how to use a default parameter value.

def function_c(name = "YY"):
    print("The bbking is " + name)

function_c()
function_c("RR")


# pass a list as an argument
def function_d(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
function_d(fruits)

# Return Values
def function_f(x):
    y = x * 2
    return y

print(function_f(3))

# The pass Statement
# function definitions cannot be empty,
# but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def empty():
    pass

'''
Recursion
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. 
It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, 
or one that uses excess amounts of memory or processor power. 
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
'''

def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0

    return result

# 6 + (6-1) + (5-1) + (4-1) + (3-1) + (2-1)
tri_recursion(6)


# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(3))
