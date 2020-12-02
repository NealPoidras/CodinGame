import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
i, j, k = 0, 0, 0
n = int(input())
while(i*5 <= n):
    j = 0
    while( j<=i and i*5+j*2<=n ):
        k = 0
        while(i*5 + j*2 +k*3 <= n):
            if (i*5+j*2+k*3) == n:
                print(i,j,k)
            k+=1
        j+=1
    i+=1


