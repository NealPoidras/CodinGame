import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
#Solved with the help of Foxx Py on Youtube.
def calculate_nb_neighboor_cell(grid,coordinates,width,height):
    i = coordinates[0]
    j = coordinates[1]
    nb_neighboor_cell = 0

    #Top cell
    if i>0 and grid[i-1][j] == "0":
        nb_neighboor_cell+=1
    #Bottom cell
    if i<height-1 and grid[i+1][j] =="0":
        nb_neighboor_cell+=1
    #Left cell
    if j>0 and grid[i][j-1] =="0":
        nb_neighboor_cell+=1
    #Right cell
    if j<width-1 and grid[i][j+1] == "0":
        nb_neighboor_cell+=1
    
    return nb_neighboor_cell
width, height = [int(i) for i in input().split()]
grid = list()
for i in range(height):
    line = input()
    grid.append(line)
for i in range(height):
    for j in range(width):
        nb_neighboor_cell = 0
        coordinates = (i,j)
        if grid[i][j] == "#" : 
            print("#",end="")
        else :
            nb_neighboor_cell +=calculate_nb_neighboor_cell(grid,coordinates,width,height)
            print(str(nb_neighboor_cell),end="")
    print()

    
