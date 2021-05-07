
def anagrame(x):
    if len(x) <= 1:
        return [x]
    elif len(x) == 2:
        return list(set([x,x[1]+x[0]]))
    else:
        return list(set([x[i] + d for i in range(len(x)) for d in anagrame(x[:i]+x[i+1:])]))

print(anagrame(input('select word : ')))