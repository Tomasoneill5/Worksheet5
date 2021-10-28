cardNum=input('please enter your card number: ')
cardNumLen=len(cardNum)
totalStep2=0
total=0
number=int(cardNum)

if (cardNumLen<13) or (cardNumLen>16):
    print('this card is invalid, must be between 13 and 16 digits')
else:
    position=1
    while number>0:
        digit= number % 10
        number= number//10
        print('******  Number is now :   ',number)
        if position % 2==0:
            digit= digit * 2
        
        if digit>=10:
            digit= (digit % 10) + 1
        
        total= digit + total
        position= position+1
        
        if (number<=9) and (number > 0):
            firstDigit=number
         
        if (number<100) and (number>=10):
            secondDigit= number % 10
   
            
print('first digit: ',firstDigit)
print('second digit: ',secondDigit)
if (firstDigit<3) or (firstDigit>6):
    print(cardNum, 'is invalid 1')
    
elif (firstDigit==3) and (secondDigit!=7):
    print(cardNum, 'is invalid 2')
    
elif  total%10!=0:
    print(cardNum, 'is invalid 3')
              
else:
    print(cardNum, 'is valid 4')
            
        
        




        
    
