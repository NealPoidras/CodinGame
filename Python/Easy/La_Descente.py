import sys
import math

while True:
    max = 0
    maxIndex = -1
    
    for i in range(8):

        mountainH = int(input())
        if mountainH > max:
            max = mountainH
            maxIndex = i


    print(maxIndex)