#recursive one
def recursive(n):
    if n==0:
        return 1
    return n*recursive(n-1)

print(recursive(int(input('choose a number : '))))

#non recursive : 
val = 1
for i in range(int(input('choose a number : ')),1,-1):
    val*=i
print(val)