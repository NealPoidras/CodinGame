import sys
import math

def verifyHowsWin(signA="",signB=""):
    if (signA == "C" and signB == "P"):
        return signA
    elif signA == "P" and signB=="R":
        return signA
    elif signA == "R" and signB == "L":
        return signA
    elif signA == "L" and signB == "S":
        return signA
    elif signA == "S" and signB == "C":
        return signA
    elif signA == "C" and signB == "L":
        return signA
    elif signA == "L" and signB == "P":
        return signA
    elif signA == "P" and signB == "S":
        return signA
    elif signA == "S" and signB == "R":
        return signA
    elif signA == "R" and signB == "C":
        return signA
    elif signA == signB:
        return "equal"
    if (signB == "C" and signA == "P"):
        return signB
    elif signB == "P" and signA=="R":
        return signB
    elif signB == "R" and signA == "L":
        return signB
    elif signB == "L" and signA == "S":
        return signB
    elif signB == "S" and signA == "C":
        return signB
    elif signB == "C" and signA == "L":
        return signB
    elif signB == "L" and signA == "P":
        return signB
    elif signB == "P" and signA == "S":
        return signB
    elif signB == "S" and signA == "R":
        return signB
    elif signB == "R" and signA == "C":
        return signB



def define_winner(tournament = [],winner = {}):
    ls =[]
    value = "equal"
    if(len(tournament)==1):
        key = winner.keys()
        vals = winner.values()
        valkey = ""
        valvalue = ""
        for k in key:
            valkey+=str(k)
        for v in vals:
            for val in v:
                valvalue+=str(val)+" "
        valvalue = valvalue[:-1]
        print(valkey+"\n"+valvalue)
        return
    for i in range(0,len(tournament)-1,2):
        value = verifyHowsWin(tournament[i][1],tournament[i+1][1])
        if(tournament[i][1]==value):
            ls.append(tournament[i])
            winner[tournament[i][0]].append(tournament[i+1][0])
            del winner[tournament[i+1][0]]
        elif(tournament[i+1][1]==value):
            ls.append(tournament[i+1])
            winner[tournament[i+1][0]].append(tournament[i][0])
            del winner[tournament[i][0]]
        else:
            #print(value,tournament[i][1],tournament[i+1][1],file=sys.stderr,flush=True)
            if(tournament[i][0]>tournament[i+1][0]):
                ls.append(tournament[i+1])
                winner[tournament[i+1][0]].append(tournament[i][0])
                del winner[tournament[i][0]]
            else:
                ls.append(tournament[i])
                winner[tournament[i][0]].append(tournament[i+1][0])
                del winner[tournament[i+1][0]]
    define_winner(tournament = ls,winner = winner)

n = int(input())
if(n%2!=0):
    exit(-1)
tournament = []
winner = {}
for i in range(n):
    numplayer, signplayer = input().split()
    numplayer = int(numplayer)
    tournament.append((numplayer,signplayer))
    winner[numplayer] = []

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
define_winner(tournament,winner)

