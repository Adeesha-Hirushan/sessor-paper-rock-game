import random

choice = input("Enter your choice (r /p /s): ")


if choice == "r":
    computer_choice = random.choice(["p", "s"])
    print(f'computer_choice = {computer_choice}')
    if computer_choice == "p":
        print("Paper covers Rock. You lose!")
    elif computer_choice == "s":
        print("Rock crushes Scissors. You win!")

elif choice == "p":
    computer_choice = random.choice(["r", "s"])
    print(f'computer_choice = {computer_choice}')
    if computer_choice == "r":
        print("Paper covers Rock. You win!")
    elif computer_choice == "s":
        print("Scissors cuts Paper. You lose!")

elif choice == "s":
    computer_choice = random.choice(["r", "p"])
    print(f'computer_choice = {computer_choice}')
    if computer_choice == "r":
        print("Rock crushes Scissors. You lose!")
    elif computer_choice == "p":
        print("Scissors cuts Paper. You win!")

else:

    print("Invalid choice. Please enter r, p, or s.")
