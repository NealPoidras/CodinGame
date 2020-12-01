import sys
import math
dict_correct = {"(":")","[":"]","{":"}"}
expression = input()
list_open = list()
correct = True

for c in expression:
    if c in dict_correct.keys():
        list_open.append(c)
    elif c in dict_correct.values():
        if len(list_open) == 0 or len(list_open) > 0 and dict_correct[list_open[len(list_open)-1]]!=c:
            correct = False
            break
        else:
            del list_open[-1]
if correct:

    correct = False if len(list_open) > 0 else True

print("true") if correct else print("false") 
"""
#Work only for case 1 to 6
print("true") if (expression.count("(") + expression.count(")")) %2 ==0 and (expression.count("[") + expression.count("]")) %2 ==0\
and (expression.count("{") + expression.count("}")) %2 ==0 else print("false")
"""