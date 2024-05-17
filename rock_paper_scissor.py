import random;
computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Do you want rock, paper, or scissors?\n")
if (computer_choice == "paper" and user_choice == "scissors"
    or computer_choice == "rock" and user_choice == "paper"
    or computer_choice == "scissors" and user_choice == "rock"):
    print("You win!, the computer choice was " + computer_choice)
elif (computer_choice == user_choice):
    print("TIE Your choice and computer choice are " + user_choice)
else:
    print("Computer Wins! Your choice is " + user_choice + " and the computer choice was", computer_choice)
