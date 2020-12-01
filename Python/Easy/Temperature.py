import sys
import math


tab = []
min = 5526
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    t = int(i)
    tab.append(t)
    
if(tab!=[]):
    tab = set(tab)

for t in tab:
    print("Element du tableau : ",t, file=sys.stderr, flush=True)
    if abs(t)<=abs(min):
        if(abs(t) == abs(min)):
            min = abs(t)
            pass
        else:
            min = t
if(tab == []):
    print(0)
else:
    print(min)

