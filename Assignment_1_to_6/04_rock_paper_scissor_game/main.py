import random

def play():
    choices: list[str] = ["Rock", "Paper", "Scissor"]

    random_number = random.randint(0,2)
    user_input = int(input("Select your choice:\n1. Rock\n2. Paper\n3. Scissor "))

    computer_choice = random.choice(choices)
    user_choice = choices[user_input - 1]

    print(f"User choice {user_choice}")
    print(f"Computer choice {computer_choice}")
    if (user_choice == computer_choice):
        print("-"*25)
        print("\tMatch tie")
        print("-"*25)
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissor" and computer_choice == "Paper")
    ):
        print("-"*25)
        print("\tYou win")
        print("-"*25)
    else:
        print("-"*30)
        print("\tCoumputer Win")
        print("-"*30)
play()