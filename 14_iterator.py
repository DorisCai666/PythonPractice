'''
Python Iterators
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
'''


# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

mytuple = ("Happy", "New", "Year", "2020")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# string

str = "2020"
myit = iter(str)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

'''
Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.
'''

#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)