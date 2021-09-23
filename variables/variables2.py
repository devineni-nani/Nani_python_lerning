#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:

a = b = c = "Orange"
print(a)
print(b)
print(c)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

#Unpack a list:

fruits = ["apple", "banana", "cherry"]
d, e, f = fruits
print(d)
print(e)
print(f)
