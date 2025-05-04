# this program is about rolling the dice and getting some random numbers

import random

while(True):
# get user input
    user_confirmation = input("Roll the dice? Y/N: ").lower()
    
    if user_confirmation == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
    elif user_confirmation == "n":
        print("thanks for playing!")
        break
    else:
        print("Invalid choice")
