# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

x = ("joe", "and", "the juice")

# convert the tuple into a list to be able to change it:
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Loop Through a Tuple
for item in x:
    print(item)

# Check if Item Exists
if "joe" in x:
    print("yes, it is.")
else:
    print("no")

# length
print(len(x))

# unchangeable, try to add one item to a tuple, it will failed.

# define a tuple, only have one item
one = ("A",)
print(type(one))
#string, not a tuple
one = ("A")
print(type(one))


# del
# The del keyword can delete the tuple completely:

del one
#print(one)
