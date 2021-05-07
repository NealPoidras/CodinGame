def tri_a_bulle(tab):

    for i in range(len(tab)-1,1,-1):
        for j in range(0,i,1):
            if tab[j] > tab[j+1]:
                tmp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = tmp

    return tab

tab = [30,12,20,9,15]
print(tri_a_bulle(tab))
