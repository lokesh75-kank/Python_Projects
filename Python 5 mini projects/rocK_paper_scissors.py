import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper","scissors"]
while True:

    user_input = input("type rock/paper/scissor or q to quit : ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock = 0 , paper = 1 , scissor = 2

    computer_picks = options[random_number]

    print("computer pick", computer_picks)

    if user_input == "rock"  and computer_picks == "paper":
        print("computer won !")
        computer_wins += 1
    elif user_input == "paper"  and computer_picks == "scissors":
        print("computer won !")
        computer_wins += 1
    elif user_input == "scissors"  and computer_picks == "rock":
        print("computer won !")
        computer_wins += 1

    else:
        print("you won !")
        user_wins += 1

print("you won ", user_wins, "times.")
print("computer won ", computer_wins, "times.")
print("Goodbye")