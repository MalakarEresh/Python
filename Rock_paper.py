import random

print("Rock, Paper, and Scissor Game")
print("Menu for the program:")
print("1. For Rock\n2. For paper\n3. For Scissor")

while True:
    choice = int(input("Make a choice: "))
    if choice in [1, 2, 3]:
        break
    else:
        print("Invalid selection. Please choose 1, 2, or 3.")

random_choice = random.randint(1, 3)

if choice == 1:
    print("You chose to go with rock")
elif choice == 2:
    print("You chose to go with paper")    
elif choice == 3:
    print("You chose to go with scissor")


if random_choice == 1:
    print("PC chose to go with Rock")
elif random_choice == 2:
    print("Pc chose to go with Paper")
elif random_choice == 3:
    print("Pc chose to go with Scissor")         


if choice == random_choice:
    print("Game ended with a draw")
elif (choice == 1 and random_choice == 2) or \
     (choice == 2 and random_choice == 3) or \
     (choice == 3 and random_choice == 1):
    print("PC wins")
else:
    print("You win")
