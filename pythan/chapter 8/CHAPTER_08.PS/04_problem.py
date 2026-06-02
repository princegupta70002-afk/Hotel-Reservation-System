'''
sun(1) = 1
sun() = 1+2
sum(3) = 1+2+3
sum(4)= 1+2+3+4


sum(n) = 1+2+3+4+....+n

sum(n) = sum(n-1) + n


'''


def sum(n):
    if(n==1):
        return 1
    return sum(n-1) +n
  
print(sum(5))    
