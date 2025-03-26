import random

print("-"*50)
print("Welcome to guess game (user)")
print("-"*50)
random_number = random.randint(1, 100)
tries = 1
user_input = int(input("Guess the Number b/w 1 - 100: "))

while random_number != user_input:
    tries += 1
    if user_input < random_number:
        print("\nYour Guess number is low")
    elif user_input > random_number:
        print("\nYour Guess number is high")
    user_input = int(input("Please Try Again: "))
        
print("-"*50)
print(f"Conratulatons! you guess the correct number {random_number} in {tries} tries\n")