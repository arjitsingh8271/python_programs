'''
eval() function in python
This is an in-built function available in python, which takes the strings as an input. The strings which we pass to it should, generally, be expressions. The eval() function takes the expression in the form of a string and evaluates it and returns the result.

Examples,
eval(’10 + 10′) → 20
eval(’10 * 10′) → 100
eval(’10 and 10′) → 10
eval(’10 or 10′) → 10
eval(‘0 and 10’) → 0
eval(’10 or 0′) → 10
eval(’10 / 10′) → 1.0
eval(’10 // 10′) → 1
eval(’10 >= 10′) → True
'''

sum = eval(input("Enter expression: "))
print(sum)


'''
OUTPUT 1:
Enter expression: 1+2*3
7

OUTPUT 2:
Enter expression: 10 and 5
5
'''