import time as t
from datetime import datetime

from random import randint
def time():
    print ('Dices are rolling')
    for i in range(2):
        t.sleep(2)
        print('.')
    print ('Summing up the values of dices')
    for i in range (2):
        t.sleep(2)
        print ('.')
        
print ('''INTRUCTION:
1) guess number between 2 to 12 only'
2) you have got three chance''')

for i in range (1,5):
    sumofdice=randint(1,6)+randint(1,6)
    print ('chance',i)
    try:
        n=int(input('Guess a number:'))
        if n<2 or n>12:
            raise ValueError
            
        if (sumofdice==n):
            time()
            print ('you won $500')
            print ('sum of dice is:',sumofdice)
        else:
            
            
            time()
                
            print ('Computer wins. Better luck next time')
            print ('sum of dice is:',sumofdice)
    except (ValueError):
        print ('guess number between 2 to 12 only')
t.sleep(1)           
print ('Thank you for playing!!!')

