# Tuple items are ordered, unchangeable, and its allow duplicate values.


tp=(1, 'mango', 2.3, 'A')
print(tp)                   #(1, 'mango', 2.3, 'A')
print(type(tp))             #<class 'tuple'>
print(len(tp))              #4

print(tp[3])                #A

#tp[0] = 1                  #error: 'tuple' object does not support item assignment

#tp.insert(1, 'apple')      #error: 'tuple' object has no attribute 'insert'

