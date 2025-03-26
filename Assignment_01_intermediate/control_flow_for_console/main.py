import random

def main():
    NUM_ROUND = 5
    score = 0

    print()
    print("Welcome to the High-Low Game!")
    print("-"* 50)
    for rounds in range(1, NUM_ROUND + 1):
        user_random = random.randint(0, 99)
        computer_random = random.randint(0, 99)
        print(f"Round {rounds}")
        print(f"Your number is {user_random}")
        user_input = input("Do you think your number is higher or lower than the computer's?: ").lower()
        if user_input == "lower" or user_input == "higher":
            if (user_random < computer_random and user_input == "lower") or (user_random > computer_random and user_input == "higher"):
                print(f"✅ You were right! The computer's number was {computer_random}")
                score += 1
            else:
                print(f"❌ Aww, that's incorrect. The computer's number was {computer_random}")
        else:
            print("🚸 Please input only 'lower' or 'higher' to make a guess")
        print(f"Your score is now {score}")
        print()
    if score == NUM_ROUND:
        print("Wow! You played perfectly!")
    elif score >= round(NUM_ROUND/2):
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")
    print()
    
if __name__ == "__main__":
    main()