import sys 
import random 
number = random.randint(1, 100) 
attempts = 0

def record_attempts(guess,number): 
    if guess<number: 
        print('Guess is too low!') 
        return False 
    elif guess>number: 
        print('Guess is too high!') 
        return False 
    else:
        return True

while True: 
    guess=input('Guess the number (1-100): ') 
    try:
        guess=int(guess) 
    except ValueError: 
        print('Please input an integer.') 
        continue 
    attempts+=1 
    if record_attempts(guess, number): 
        break 

print('You got it after '+str(attempts)+' attempts!') 
