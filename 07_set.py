# A set is a collection which is unordered and unindexed.
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

# Create a Set:
myset = {"apple", "orange", "kiwi", "celery"}
print(myset)

# look through
for item in myset:
    print(item)

# Add Items
# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.
myset.add("grapes")
myset.update({"watermelon","tomato"})
print(myset)

# If the item to remove does not exist, remove() will raise an error.
myset.remove("apple")
# myset.remove("Noname")
# If the item to remove does not exist, discard() will NOT raise an error.
myset.discard("NOname")
print(myset)
# If use pop method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.
myset.pop()
print(myset)

# The clear() method empties the set.
clearset = {"a", "b", "c"}
clearset.clear()
print(clearset)

# The del keyword will delete the set completely
delset = {"a", "b", "c"}
del delset
#print(delset)

# Join Two Sets
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another.

set1 = {3, 2, 0}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"1", "3" , "6"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

