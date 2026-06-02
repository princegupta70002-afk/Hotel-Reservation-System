def divisibles5(n):
    if(n%5 == 0):
         return True
    return False 

a =  [1,324,35,5778, 59,25,436,235,34,2346,66,5,33,3546,5778]

f =  list(filter(divisibles5, a))

print(f)
