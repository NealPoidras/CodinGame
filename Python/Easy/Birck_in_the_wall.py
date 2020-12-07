import sys
import math

X = int(input())
N = int(input())
M = sorted(map(int,input().split()),reverse=True)
print(format(sum([(i//X)*0.65*M[i] for i in range(N)]),".3f"))