#Write a program to swap the values of two variables without using any arithmetic operators. Given a=10, b=20 Expected o/p:- a=20, b=10

import sys

# write your answer here
a=int(input())
b=int(input())

t=a
a=b
b=t

print("a={}".format(a))
print("b={}".format(b))