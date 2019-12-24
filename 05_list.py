'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type.

Choosing the right type for a particular data set could mean retention of meaning, and,
it could mean an increase in efficiency or security.  '''

### List ###

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

listexample = ["Mike", "Doris", "Sophie","Richard","Edan"]
print(listexample)
print(listexample[1])
print(listexample[-1])

# Range of index
print(listexample[1:2])
print(listexample[:4])

# Change item:
listexample[0] = "Tom"
print(listexample)

# Look through
for x in listexample:
    print(x)

# Check if
listexample = ["Mike", "Doris", "Sophie", "Richard", "Edan"]
if "Sophie" in listexample:
    print("Yes, 'Sophie' is here")

# Length

print(len(listexample))

# Add iteam
# Append
listexample.append("Emma")
print(listexample)

# Insert
listexample.insert(1, "Jay")
print(listexample)

# Remove
listexample.remove("Jay")
print(listexample)

# Pop
listexample.pop()
print(listexample)

# Del
del listexample[0]
print(listexample)

# Copy
listexample = ["Mike", "Doris", "Sophie", "Richard", "Edan"]
listone = listexample.copy()
print(listone)
listtwo = list(listexample)
print(listtwo)

# Join Two Lists
# There are several ways

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# or
for x in list2:
    list1.append(x)
print(list1)

# or
list1.extend(list2)
print(list1)



