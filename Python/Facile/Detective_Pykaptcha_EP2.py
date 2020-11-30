import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
#Following the video of foxx py on youtube. To understand more how to do.
#Not just copying the code, try to understand how to do it ! :D 


def define_cycle(side,direction_pika):
    directions = ["<","^",">","v"] if side == "L" else ["v",">","^","<"]
    index_directions = directions.index(direction_pika)
    if index_directions > 0:
        directions = directions[index_directions-1:len(directions)] + directions[0:index_directions-1]
    else :
        directions = directions[3:]+directions[0:3]
    return directions


def instantiate_multi_line_grid(height,width):
    grid = list()
    for i in range(height):
        line_list = list()
        for j in range(width):
            line_list.append(0)
        grid.append(line_list)
    return grid

def move(grid,start_point,side,height,width):
    i = start_point[0]
    j = start_point[1]
    direction_pika = start_point[2]

    directions = define_cycle(side,direction_pika)

    for k in directions :
        #Left
        if k == "<" and j > 0 and (grid[i][j-1] == "0" or grid[i][j-1] in directions):
            start_point = (i, j-1, "<", True)
            break
        #Right
        if k == ">" and j < width-1 and (grid[i][j+1] == "0" or grid[i][j+1] in directions):
            start_point = (i, j+1, ">", True)
            break
        #Top
        if k == "^" and i > 0 and (grid[i-1][j] == "0" or grid[i-1][j] in directions):
            start_point = (i-1, j, "^", True)
            break
        #Bottom
        if k == "v" and i < height-1 and (grid[i+1][j] == "0" or grid[i+1][j] in directions):
            start_point = (i+1, j, "v", True)
            break
    return start_point

def display_test(grid,height,width): 
    for i in range(height):
        for j in range(width):
            print(final_grid[i][j],end="",file = sys.stderr,flush=True)
        print(file=sys.stderr,flush=True)

width, height = [int(i) for i in input().split()]
grid = list()
final_grid = instantiate_multi_line_grid(height,width)
start_point = tuple()#(num_line,nu_column,direction,end_maze)
end_maze = False


#instanciation of grid and filling final_grid with walls("#")
for i in range(height):
    line = input()
    grid.append(line)

    #We are looking for the start point and the direction Pikachu is looking at
    for direction in ["<","^",">","v"]:
        for j in range(len(line)):
            if direction == line[j]:
                start_point = (i,j,direction,False) #fix the starting point


    for j in range(len(line)):
        if grid[i][j] == "#" :
            final_grid[i][j] = "#"
    
side = input()
while(end_maze==False):
    start_point = move(grid, start_point, side, height, width)
    i = start_point[0]
    j = start_point[1]

    if(start_point[3] == True):
        final_grid[i][j] += 1

    if grid[i][j] in ["<","^",">","v"] : 
        end_maze = True
    """print("New one: ",file = sys.stderr,flush=True)
    display_test(final_grid,height,width)"""

for i in range(height):
    for j in range(width):
        print(final_grid[i][j],end="")
    print()