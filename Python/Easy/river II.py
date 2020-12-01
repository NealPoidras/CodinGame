import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#Bibou code codingGame
def river(r):
    return r+sum(int(x) for x in str(r))

r_1 = int(input())
canBeaMeetingPoint = "NO"
for i in range(1,r_1):
    r = river(i)
    if r == r_1:
        canBeaMeetingPoint = "YES"
        break
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(canBeaMeetingPoint)
