#sum of list
def sum_of_list(l):
    if len(l):
            return l[0]+sum_of_list(l[1:])
    return 0

l=[1,2,3,4,5]
print(sum_of_list(l))
'''
1+[2,3,4,5]
2+[3,4,5]
3+[4,5]
4+[5]
5+[]
0'''
