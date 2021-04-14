def KnowTheRightBackAMount(cash=0):  #this one  has a default for 11, and many other exception.
    ten = 0
    five= 0
    two = 0
    if(cash==1 or cash ==3):
        return None
    if cash >=10 :
        ten = int(cash/10)
        if (cash%10)%5 !=0:
            five = int((cash%10)/5)
            if ((cash%10)%5)%2 == 0:
                two = int((cash%10)%5)/2
            else:
                if (cash%10)%2 ==0:
                    five = 0
                    two = int((cash%10)/2)  
        else:
            if(cash%10)%5 == 0:
                five = int(cash%10)/5
            elif (cash%10)%2 == 0 :
                two = int((cash%10)/2)
    elif(cash >= 5):
        five = int(cash/5)
        if (cash%5)%2 == 0 :
            two = int((cash%5)/2)
        else:
            if cash%2==0 :
                five = 0
                two = int(cash/2)
    elif(cash>=2):
        two = int(cash/2)
    return {
        'two':two,
        'five':five,
        'ten':ten
    }

def KnowTheRightBackAMountBis(cash = 0):#This works for each case.
    ten  = 0
    five = 0
    two = 0
    if cash>=5:
        if cash%5 !=0:
            five = int(cash//5)
            cash -=five*5
            if cash%2 !=0:
                cash+=5
                five-=1
                two = int(cash//2)
            else : 
                two = int(cash//2)
        else :
            five = cash//5 
    if five //2 >0:

        ten =  five//2
        five = five%2

    return {"two":two,"five:":five,"ten:":ten}

print(KnowTheRightBackAMountBis(int(input("choose You're amount of money : "))))