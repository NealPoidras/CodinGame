import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def recherche_valeur_decimale_alphabet(t):
    L = [x for x in range(65,91)]
    liste_place_alphabet = list()
    for lettre in t:
        if ord(lettre.upper()) in L:
            liste_place_alphabet.append(L.index(ord(lettre.upper())))
        else:
            liste_place_alphabet.append(26)
    return liste_place_alphabet
l = int(input())
h = int(input())
t = input()

liste_place_alphabet = recherche_valeur_decimale_alphabet(t)
for i in range(h):
    row = input()
    answer = ""
    for pos_alpha in liste_place_alphabet:
        answer+= row[pos_alpha*l:pos_alpha*l+l]
        print(answer, file=sys.stderr, flush=True)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(answer)
