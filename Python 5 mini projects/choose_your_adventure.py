name = input("Enter your name ")

print("Welcome to adventure game ", name)

chose_adventure = input("you have entered the Amazon jungle, please take right or left turn, Enter your anwser :")

if chose_adventure == "left":
    left = input("you need to cross the river now to go across it, please type yes/No ").lower()

    if left == "yes":
        print("you were eaten by allegator, you lose ! ")

    else:
        print("you were eaten by tiger, you lose !")

if chose_adventure == "right":
    right = input("you need to climb the mountain, ready ? yes/No ").lower()

    if right == "yes":
        print("you have successfully climbed the mountain and reached your destination, you won !")
    else:
        print("you are coward , you lose")
    
print("Thank you for playing", name)

