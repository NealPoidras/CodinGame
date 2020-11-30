import sys
import math

def def_rotation_cycle(rotation):
    if 'x' in rotation:
        return ["U","B","D","F"]
    elif 'y' in rotation:
        return ["L","B","R","F"]
    else:
        return ["U","R","D","L"]

def apply_rotation(face,rotation):
    clockwise = False if "'" in rotation else True
    rotation_cyle = def_rotation_cycle(rotation)


    if face in rotation_cyle:
        index_face = rotation_cyle.index(face)
        if index_face < len(rotation_cyle)-1 and clockwise:
            return rotation_cyle[index_face+1]
        elif index_face == len(rotation_cyle)-1 and clockwise:
            return rotation_cyle[0]
        elif index_face > 0 and not clockwise:
            return rotation_cyle[index_face-1]
        elif index_face == 0 and not clockwise:
            return rotation_cyle[len(rotation_cyle)-1]
    else:
        return face
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rotations = input().split(" ")
face_1 = input()
face_2 = input()

for rotation in rotations:
    face_1 = apply_rotation(face_1,rotation)
    face_2 = apply_rotation(face_2,rotation)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(face_1)
print(face_2)
