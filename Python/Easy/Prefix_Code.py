import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def convert_str(word,bin_ascii):
    new_word = ""
    tmp = ""
    for w in word :
        tmp+=w
        for key,value in bin_ascii.items():
            if(tmp == key):
                new_word+=chr(value)
                tmp=""
                break
    if(len(new_word)==0):
        return "DECODE FAIL AT INDEX 0"
    if(len(tmp)>0):
        return "DECODE FAIL AT INDEX "+str(len(word)-1)    
    return new_word

bin_ascii = {}
n = int(input())
if(n<1):
    print("DECODE FAIL AT INDEX 0")
else :
    for i in range(n):
        Binary,Ascii = input().split()
        Ascii = int(Ascii)
        bin_ascii[Binary] = Ascii
    s = input()
    for key,value in bin_ascii.items():
        print(key,value, file=sys.stderr, flush=True)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(convert_str(s,bin_ascii))
