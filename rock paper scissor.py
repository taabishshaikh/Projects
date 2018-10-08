import time as t
from datetime import datetime
import random
rps=['rock','paper','scissor']
def time():
    for i in range (2):
        t.sleep(1)
        print ('.')

p=0
c=0
d=0
for i in range (1,6):
    print ('chance',i)
    w=input('choose rock, paper or scissor: ')
    player=w.lower()
    if player != 'rock' and player != 'paper' and player != 'scissor':
        print ('enter proper choice')
        break
    
    computer = random.choice(rps)
    print ('Computer chose...')
    time()
    print (computer)
    if player==computer:
        print ('draw')
        d+=1
#-------------player winning-------
    elif computer=='rock' and player=='paper' or computer == 'paper' and player == 'scissor' or computer == 'scissor' and player == 'rock':
        print ('You won')
        
        p+=1
#-------------computer winning------
    
    elif computer == 'rock' and player == 'scissor' or computer == 'paper' and player == 'rock' or computer =='scissor' and player == 'paper':
        print ('Computer won')
        c+=1
    else:
        pass
    t.sleep(2)

print ('Game Sumamry')
print ('Drawn',d,'times')
print ('Player won',p,'times')
print ('Computer won',c,'times')
t.sleep(3)
print ('Thank you for playing')
