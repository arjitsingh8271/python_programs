'''
Command Line Arguments in Python:

The command we are executing thorough is command prompt/terminal. 
The script is invoked with this command and the execution starts. 
While invoking the script we can pass the arguments to it, which are called command-line arguments. 
Arguments are nothing but parameters or values to the variables.

Our command is ‘python’ and the ‘filename.py’ ‘10’ ‘20’ are arguments to it. 
In order to use these arguments in our script/code, we should do the following import

from sys import argv

After including the above import statement in our file, the arguments 
which we pass from the command are available in an attribute called ‘argv’. 
argv will be a list of elements that can be accessed using indexes.

argv[0] will always be the filename.py
argv[1] will be 10 in this case
argv[2] will be 20 in this case
'''

from sys import argv
print(argv[0])
print(argv[1])
print(argv[2])



'''
/python_programming$ python3 command_line_arguments_01 10 20

OUTPUT:
10
20

'''