import sys
import math

def digitSquare(nb):
    sq = 0; 
    while (nb!=0): 
        digit = nb % 10
        sq += digit * digit 
        nb = nb // 10        
    return sq; 

def isHappy(n):
    s = set()
    s.add(n)
    while (True): 
        if (n == 1): 
            return True   
        n = digitSquare(n) 
        if n in s: 
            return False
        s.add(n) 
    return False 

n = int(input())
s = []
for i in range(n):
    x = input()
    s.append(int(x))

for element in s:
    if(isHappy(element)==False):
        print(element,":(")
    else:
        print(element,":)")
