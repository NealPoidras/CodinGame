import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
my_dict = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    my_dict[ext.upper()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    try:
        indexOfDot = fname.rindex(".")
        tmp = str(fname[indexOfDot+1:len(fname)]).upper()
        try:
            print(my_dict[tmp])
        except:
            print("UNKNOWN")
    except:
        print("UNKNOWN")

