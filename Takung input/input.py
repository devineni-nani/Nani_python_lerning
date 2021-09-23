'''This function first takes the input from the user and then evaluates the expression, 
which means Python automatically identifies whether user entered a string or a number or list. 
If the input provided is not correct then either syntax error or exception is raised by python.'''
#input() use
roll_num= input("enter your roll number:")
print (roll_num)

'''
How the input function works in Python :

When input() function executes program flow will be stopped until the user has given an input.
The text or message display on the output screen to ask a user to enter input value is optional i.e. 
the prompt, will be printed on the screen is optional.
Whatever you enter as input, input function convert it into a string. 
if you enter an integer value still input() function convert it into a string. You need to explicitly convert it into an integer in your code using typecasting.
for example:
    '''
num=input("enter an number:")
print (num)
name = input ("enter your name:")
print (name)
#Printing type of input value
print ("type of num", type(num))
print ("type of name:", type(name))
num1=type(num)
print ("after typecasting num type:", type(num1))
