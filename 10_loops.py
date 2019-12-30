### The while Loop ###
# With the while loop we can execute a set of statements as long as a condition is true.

# Print i as long as i is less than 6:
# remember to increment i, or else the loop will continue forever.
i = 1
while i < 6:
  print(i)
  i += 1

#The break Statement
print("break example")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement
print("continue example")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else Statement
# Print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


### Python For Loops ###

names = ["LL", "RR", "YY"]
for x in names:
    print(x)

# loop through a string
text = "I lost my heart in SanFrancisco"
for x in text:
    print(x)

# break
names = ["LL", "RR", "YY"]
for x in names:
    if x == "RR":
        break
    print(x)

# continue
# break

names = ["LL", "RR", "YY"]
for x in names:
    if x == "LL":
        continue
    print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(2, 6):
    print(x)

for x in range(4):
    print(x)

# Increment the sequence with 3 (default is 1):
for x in range(1, 30, 3):
    print(x)

# else
for x in range(3):
    print(x)
else:
    print("Finally finished!")

### Nested Loops

colors = ["red", "yellow", "green"]
cars = ["Toyota", "Honda", "Benz"]

for color in colors:
    for car in cars:
        print(color,car)


# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.

for x in [0,2,3]:
    pass