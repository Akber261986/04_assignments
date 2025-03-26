import random
import time

random_num = random.randint(0, 99)
print("I am thinking of a number between 0 and 99...", end=" ")

def main():
    try:
        user_input = int(input("Enter a guess: "))
        while True:
            if user_input == random_num:
                print("-"*50)
                print(f"Congrats! The number was: {random_num}")
                print("-"*50)
                break
            elif user_input < random_num and user_input >= 0:
                print("Your guess is too low")
            elif user_input > random_num and user_input < 100:
                print("your guess is too high")
            else:
                print("Number Should be between 0-99")
            user_input = int(input("Enter a New number: "))
    except ValueError :
        print("\nError! Input must be an integer")
        print("The Game is Restarting... \n")
        time.sleep(3)
        main()


if __name__ == "__main__":
    main()