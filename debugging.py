# A program to enter the marks of a student in four subject
import pdb

pdb.set_trace()
# l :  list were u are
# n :  to run that part
# c :  normal run
# q :  exit

marks1 = int(input("Enter the marks in Physics: "))
marks2 = int(input("Enter the marks in Chemistry: "))
marks3 = int(input("Enter the marks in Maths: "))
marks4 = int(input("Enter the marks in English: "))
marks5 = int(input("Enter the marks in Fine Arts: "))

total = marks1+marks2+marks3+marks4+marks5
per = float(total)/500 * 100

print("Total = ",total, "\t Percenteg = ",per)