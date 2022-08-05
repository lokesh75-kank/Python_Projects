from random import random

import random


random_number = input("Enter the any number ! ")

if random_number.isdigit():
    random_number = int(random_number)
   
    if random_number <= 0:
        print("Enter number greater then 0 ")
else:
    print("Enter the number again ")
    

generate_random_number = random.randint(0, random_number)
guesses = 0

while True:
    guesses += 1

    user_guessing = input("Guess the number !")

    if user_guessing.isdigit():
        user_guessing = int(user_guessing)
    else:
        print("Please enter a number next time")
        continue

    if user_guessing == generate_random_number:
        print("you got it ")
        break

    elif user_guessing > generate_random_number:
        print("your guess is greater then random number")
        
    else:
        print("your guess is lower then random number")
    continue

print("You guess the correct no in " , guesses , "chances")
