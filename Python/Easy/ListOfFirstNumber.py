def defineFirstNumber(n):
    if n<1:
        return False
    if int((n-1)/2)<2:
        return False
    for i in range(2,int((n-1)/2),1):
        if n%i == 0:
            return False
    return True

def getListFirstNumber(n):
    ls = [1,2,3]
    for i in range(1,n,1):
        if defineFirstNumber(i):
            ls.append(i)
    return ls

print(getListFirstNumber(int(input('Choose a number to get all first Number before this one him included : '))))