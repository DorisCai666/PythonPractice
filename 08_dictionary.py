# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

# create a dictionary

mydict= {
    "name": "Doris",
    "city": "SF",
    "year": 2019
}
print(mydict)

# get value from a key
print(mydict["year"])
print(mydict.get("year"))

# change a value by key
mydict["year"] = 2018
print(mydict)

# look through
for x in mydict:
  print(mydict[x])

for x in mydict.values():
  print(x)

for x,y in mydict.items():
  print(x,y)


# Adding items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
mydict["color"] = "Green"
mydict["Instrument"] = "Guitar"
print(mydict)

# Copy a Dictionary
copydict = mydict.copy()

# remove items
# the popitem() method removes the last inserted item
copydict.pop("color")
print(copydict)
copydict.popitem()
print(copydict)
del copydict["name"]
del copydict

# Nested Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
