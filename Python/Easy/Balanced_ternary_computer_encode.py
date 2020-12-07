import sys
import math

def encode(number):
    if number<0:
        BT = encode(number = -number)
        return ''.join(['1' if c == 'T' else ('T' if c == '1' else '0') for c in BT])
    if number == 0 :
        return ''
    if number % 3 == 2:
        return encode(number = (number+1)//3) + 'T'
    else:
        return encode(number = number//3) + str(number %3 )

n = int(input())
print(encode(n)) if n !=0 else print("0")