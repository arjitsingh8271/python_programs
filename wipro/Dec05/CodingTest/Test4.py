"""
Write a function to check whether a number is a perfect number. A perfect number is defined as the positive number in which the sum of all positive divisors excluding the number itself is equal to that number.
a. Ex: 6 the divisor of 6 is 1,2,3 and 1+2+3=6
b. 28 the divisors of 28 is 1,2,4,7,14 and 1+2+4+7+14=28
"""


def is_perfect_number(number):
    
    if number <= 0:
        return False
    
    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    
    return divisor_sum == number


num=int(input())

if is_perfect_number(num):
    print("{} is perfect".format(num))
else:
    print("{} is not perfect".format(num))