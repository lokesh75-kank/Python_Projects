# Beginner level project online quize game- 08/7/22

print("Welcome to online cricket quize")

enter = input("Enter you name " )
print("Welcome to online cricket quize " + enter + ", Lets Begin !")

score = 0

enter = input("When was 1st one day cricket happened ? ")
if enter == "1950":
    print("Correct !")
    score += 1
else:
    print("Incorrect !")

enter1 = input("Who won the 2021 cricket world cup ? ")
if enter1.lower() == "England":
    print("Correct !")
    score += 1
else:
    print("Incorrect !")

enter = input("where was world cup 22 final held ? ")
if enter == "England":
    print("Correct !")
    score += 1
else:
    print("Incorrect !")

print("Total score you got " + str(score) + "Congratulations")