# If we have defined a variable in a function. 
#    Then that variable will be accessible only in that function.
def fun_name():
   name="Devineni is local variable"
   print(name)
fun_name()
#when we call the function, the control is transferred to the function where the variable named 'name' gets initialized and printed.
#As soon as the function exits and passes the control back to the main program, the variable 'name' is no longer in scope.
#This is how a local variable behaves, and is scope lies in local to the piece of code where it’s defined
'''What will happen if we try to print the variable 'name' outside of the function?'''
#ans) name is not define