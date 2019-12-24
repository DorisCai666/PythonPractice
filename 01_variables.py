"""
A Python variable is a reserved memory location to store values.
In other words, a variable in a python program gives data to the computer for processing.

"""

class variables(object):

    # Declare a variable and initialize it
    # a,b are global in scope
    a = "Python "
    b = "is great"
    c = 0
    print("a is global variable, value is s%", a)
    print("c is global variable, value is d%", c)

    # In python the single underscore "_" is used to indicate, that a method or variable is not considered as part of the public api of a class
    # and that this part of the api could change between different versions.
    _d = 1

    # The double underscore "__" does not mean a "private variable".
    # You use it to define variables which are "class local" and which can not be easily overidden by subclasses. It mangles the variables name.
    __f = 2

    # delete a variable
    del c

    def localvar(self):
        # a is again declared in function and assumes local scope.
        a = "Doris "
        print("a is local variable, value is s%", a)


if __name__ == "__main__":
    variables = variables();
    variables.localvar()
    print(variables._d)












