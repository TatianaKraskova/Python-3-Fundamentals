import random

# Computer randomly chooses rock, paper, or scissors
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)


# User input
user_choice = input("Do you want rock, paper, or scissors? ").lower()

# Determine the winner
if computer_choice == user_choice:
    print(f"TIE! Both chose {computer_choice.capitalize()}.")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print(f"WIN! You chose {user_choice.capitalize()} and the computer chose {computer_choice.capitalize()}.")
elif user_choice in choices:
    print(f"You lose! You chose {user_choice.capitalize()} and the computer chose {computer_choice.capitalize()}.")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
