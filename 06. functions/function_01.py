'''
What is a Function?
A function is one that contains a group of statements or a block of code to perform a certain task. The advantages of using 
functions are:

Maintaining the code is an easy way.
Code re-usability.


Types of functions in python:
There are many categories based on which we can categorize the functions. This categorization is based on who created it.

Pre-defined or built-in functions
User-defined functions
Predefined or built-in functions: The functions which come installed along with python software are called predefined 
or built-in functions. We have covered some inbuilt functions in examples of earlier chapters. 
Some of them are id(), type(), input(), print() etc.

User-defined functions: The functions which are defined by the developer as per the requirement are called user-defined functions. 
In this chapter, we shall concentrate on these kinds of functions that are user-defined.


FUNCTION RELATED TERMINOLOGY
1. def’ keyword – Every function in python should start with the keyword ‘def’. 
In other words, python can understand the code as part of a function if it contains the ‘def’ keyword only.
2. Name of the function – Every function should be given a name, which can later be used to call it.
3. Parenthesis – After the name ‘()’ parentheses are required
4. Parameters – The parameters, if any, should be included within the parenthesis.
5. Colon symbol ‘:’ should be mandatorily placed immediately after closing the parentheses.
6. Body – All the code that does some operation should go into the body of the function. 
The body of the function should have an indentation of one level with respect to the line containing the ‘def’ keyword.
7. Return statement – Return statement should be in the body of the function. It’s not mandatory to have a return statement.
'''


# defining a function
def display():
    print("Function")

# calling function
display()
display()
display()



'''
OUTPUT:
Function
Function
Function
'''