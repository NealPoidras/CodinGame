import sys
def definePower(tab = []):
    tab.sort()
    if(len(tab) <=1):
        return None
    min = sys.maxsize
    for i in range(1,len(tab)):
        if(min>tab[i]-tab[i-1]):
            min = tab[i]-tab[i-1]
    return min

tab = [int(input()) for i in range(int(input()))]
print(definePower(tab))