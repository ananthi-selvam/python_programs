import random

#getting user input
while True:
    user_choice = input("Rock, paper, scissors? (R/P/S): ").lower()
    choices = ('r', 'p', 's')

#check choice is valid
    if user_choice not in choices:
        print('invalid choice')
        continue

#display choice of user and computer
    computer_choice = random.choice(choices) 
    print(f'you chose {user_choice}')
    print(f'computer chose {computer_choice}')

#determine the winner    
    if (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 's')):
        print("you win!!")
        
    elif user_choice == computer_choice:
        print('tie')
    else:
        print("computer win!!")

#ask to continue the game?
    should_continue = input("contiue? (y/n): ").lower()
    if should_continue == "n":
        print('thank you!!')
        break
