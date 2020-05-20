# This is a guess the number game
import random
print('Hello. What is your name?')
name = input()

secretNumber = random.randint (1, 20)
print ('Well, ' + name + ', I am thinking of a number between 1 and 20...')

#Ask the player to guess 6 times.
for guessesTaken in range (1,7):
    print('Take a guess!')
    guess  = int(input())
    if guess < secretNumber:
        print('Your guess is too low man...')
    elif guess > secretNumber:
        print('Your guess is way to high bro!!!')
    else:
        break #This conditions is the correct guess!

if guess == secretNumber:
    print('Good job ' + name + '! You guessed the number we had in mind... Your a mind reader bro you guesssed it in ' +  str(guessesTaken) + ' guesses!')
else:
    print('Nope. Sorry the number I was thinking of was ' + str(secretNumber) + ' sorry!!!')
