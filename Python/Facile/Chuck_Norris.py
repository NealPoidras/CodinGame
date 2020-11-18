message = input()

new_msg = ''

for i in range(len(message)):
    charInnew_msg = str(bin(ord(message[i])))[2:]
    

    charInnew_msg = charInnew_msg.zfill(7)
    
    new_msg += charInnew_msg


lastChar = ' '
codedmessage = ''
encodedBits = [' 00 0', ' 0 0']

for i in range(len(new_msg)):
    if new_msg[i] != lastChar:
        lastChar = new_msg[i]
        codedmessage += encodedBits[ord(lastChar) - ord('0')]
    else:
        codedmessage += '0'


print(codedmessage[1:])
