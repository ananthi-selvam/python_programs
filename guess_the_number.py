# This program is about to guess the number Game
import random

Name = input("Your Name: ")
print('Welcome to the guessing game ' + Name)

secertNumber = random.randint(1, 10)
print('Guess the number between 1 to 20')

for guessTaken in range(1, 6):
    guess = int(input('Take a Guess \n'))
    if guess > secertNumber:
        print('Your guess is too high!!')
    elif guess < secertNumber:
        print('your guess to low!!!')
    else:
        break

if guess == secertNumber:
    print('That was right ' + str(secertNumber))

print('You have identified the seceret number in ' + str(guessTaken) + ' Guess')


