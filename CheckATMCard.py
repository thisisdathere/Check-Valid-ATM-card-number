cardNum=input('input the card number: ')
evenPosNum=''
for i in range(0,len(cardNum),2):
    evenPosNum+=str(int(cardNum[i])*2)
S=0
for i in range(len(evenPosNum)):
    S+=int(evenPosNum[i])
for i in range(1,len(cardNum),2):
    S+=int(cardNum[i])
if S%10==0:
    print('Card is regconized')
else:
    print('Invalid number')