import sys
import math


n = int(input())
xthen_commands = input().split(";")
pos_car = int(xthen_commands[0])-1
del xthen_commands[0]
repeat = 0
direction = str()
for i in range(n):
    rthen_roadpattern = input().split(";")

    for j in range(int(rthen_roadpattern[0])):

        repeat = int(xthen_commands[0][:-1])

        if len(xthen_commands)>0:
            direction = xthen_commands[0][len(xthen_commands[0])-1]

        if direction == "R":
            pos_car+=1

        elif direction == "L":
            pos_car-=1
        
        xthen_commands[0] = xthen_commands[0].replace(str(repeat),str(repeat-1))

        if repeat == 1:
            del xthen_commands[0]

        for k in range(0,len(rthen_roadpattern[1])):
            if k== pos_car:
                print("#",end="")
            else:
                print(rthen_roadpattern[1][k],end="")
        print()