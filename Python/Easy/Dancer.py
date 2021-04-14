def position(n =0): #to calculate a position.
    return[0,1,-1,-4,-5,-3][n%6]

def stage(n=0):#to calcultate a stage 
    return[3,1,-2,-3,-1,2][n%6]


print("the position of the dancer is : ",position(int(input("ask an index : "))))

