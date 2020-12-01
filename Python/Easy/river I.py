import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def separate(number):
    number_str = str(number)
    for nb in range(len(number_str)):
        number += int(number_str[nb])
    return number

r_1 = int(input())
r_2 = int(input())
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
while(r_1!=r_2):

    if(r_1<r_2):
        r_1 = separate(r_1)
    else:
        r_2 = separate(r_2)


print(r_1)