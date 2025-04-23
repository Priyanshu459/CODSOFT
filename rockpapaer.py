import random


print("Select from the following:\n 1: Stone \n 2: Paper\n 3: Scisor")


user_input = input("Enter the value: ")

if user_input == "1":
    user_input = "Stone"
elif user_input == "2":
    user_input = "Paper"
elif user_input == "3":
    user_input = "Scisor"
else:
    print("Invalid input.")
    exit()

choices = ["Stone", "Paper", "Scisor"]
computer_choice = random.choice(choices)


count_system = 0
count_player = 0


if user_input == computer_choice:
    print("Game is a tie")
elif (user_input == "Stone" and computer_choice == "Scisor"):
    print("You win")
    count_player += 1
elif (user_input == "Paper" and computer_choice == "Stone"):
    print("You win")
    count_player += 1
elif (user_input == "Scisor" and computer_choice == "Paper"):
    print("You win")
    count_player += 1
else:
    print("Computer wins")
    count_system += 1


print(f"Your choice: {user_input}")
print(f"Computer's choice: {computer_choice}")
print(f"Your score: {count_player} | Computer score: {count_system}")
