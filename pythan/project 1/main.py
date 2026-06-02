import random

# Mapping
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# User input
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

if youstr not in youDict:
    print("Invalid input!")
    exit()

you = youDict[youstr]
computer = random.choice([1, -1, 0])

print(f"You chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

# Game Logic
if computer == you:
    print("It's a draw!")

elif (you == 1 and computer == -1) or \
     (you == -1 and computer == 0) or \
     (you == 0 and computer == 1):
    print("You win!")

else:
    print("You lose!")
      