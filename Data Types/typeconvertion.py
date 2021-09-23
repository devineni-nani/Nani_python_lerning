'''
Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:

Example
Convert from one type to another:'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Note: You cannot convert complex numbers into another number type.

#Specify a Variable Type
'''
There may be times when you want to specify a type on to a variable. 
This can be done with casting. Python is an object-orientated language, 
and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals'''
#Example
#Integers:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#Example
#Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#Example
#Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

