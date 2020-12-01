import sys
import math

class Candle:
    def __init__(self,pos,l):
        self.pos = pos
        self.l = l

    def light_room(self,pos,list_lighted_cell,l,n):
        i = pos[0]
        j = pos[1]
        if i >= 0 and j >= 0 and i < n and j < n:

            if list_lighted_cell[i][j].l == 0 : 
                list_lighted_cell[i][j].l = l
                list_lighted_cell[i][j].light_by_candle = self

            elif list_lighted_cell[i][j].l > 0 and not self.same_candle(list_lighted_cell[i][j].light_by_candle):
                list_lighted_cell[i][j].l = self.l

            elif list_lighted_cell[i][j].l <l and self.same_candle(list_lighted_cell[i][j].light_by_candle):
                list_lighted_cell[i][j].l = l

            l = l-1
            if l > 0 :
                for k in [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]:
                    list_lighted_cell = self.light_room(k,list_lighted_cell,l,n)

        return list_lighted_cell
        
    def same_candle(self,another_candle):
        return True if self.pos == another_candle.pos else False

class Cell : 
    def __init__(self,pos):
        self.pos = pos
        self.l = 0
        self.light_by_candle = None

n = int(input())
l = int(input())
list_candle = list()
list_lighted_cell = list()
nb_dark_spot = 0
for i in range(n):
    line_cell = list()
    line = input().split(" ")
    for j in range(n):
        if "C" in line[j]:
            list_candle.append(Candle((i,j),l))
        line_cell.append(Cell((i,j)))
    list_lighted_cell.append(line_cell)   

for candle in list_candle:
    list_lighted_cell = candle.light_room(candle.pos,list_lighted_cell,l,n)

for line_cell in list_lighted_cell:
    for cell in line_cell:
        if cell.l ==0:
            nb_dark_spot+=1
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(nb_dark_spot)
