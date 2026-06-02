from functools import reduce
l =  [1,34,35,778, 59,256,23,34,23,66,5,33,36,58]

def greater(a,b):
    if (a>b):
        return a
    return b
print(reduce(greater,l))




