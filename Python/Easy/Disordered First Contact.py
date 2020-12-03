import sys
import math

def define_list_num_character(message):
    sum_j,j = 1,1
    list_j=list()
    while(sum_j<=len(message)):
        list_j.append(j)
        j=j+1
        sum_j+=j
    list_j.append(len(message)-sum(list_j))
    return list_j

def encode(message,n):
    list_j = define_list_num_character(message)
    for i in range(n):
        final_message = ""
        begin = False
        for j in list_j:
            if begin:
                final_message = message[:j] + final_message
            else:
                final_message = final_message + message[:j]
            message = message[j:]
            begin = True if begin == False else False
        message = final_message
    return message

def decode(message,n):
    list_j = define_list_num_character(message)
    for i in range(n):
        begin = True if len(list_j)%2 == 0 else False
        final_message = ""
        for j in list_j[::-1]:

            if begin:
                final_message = message[:j] + final_message
                message = message[j: ]

            else:
                final_message = message[len(message)-j:] + final_message
                message = message[:len(message)- j]

            begin = True if begin == False else False

        message = final_message
    return message     


    return message
n = int(input())
final_message = decode(input(),n) if n > 0 else encode(input(),abs(n))
print(final_message)
