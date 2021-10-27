import random
import math

num1=int(input('Please enter your first number: '))
num2=int(input('Please enter your second number: '))
while num1==num2:
    num2=int(input('Numbers are equal. Please enter a different number: '))

if num1>num2:
    upper=num1
    lower=num2

else:
    upper=num2
    lower=num1
randomChoice= random.randint(lower, upper)

print(randomChoice)
minNumberGuesses= round(math.log(upper - lower +1,2))
print("min is ",minNumberGuesses)
count=0
while minNumberGuesses>count:
    count= count+1
    numGuess=int(input('Guess the number:' ))
    if randomChoice==numGuess:
        print('correct after', count,'guess(es)' )
        break
    else:
        print('incorrect after', count,'guess(es)' )

        

    



             