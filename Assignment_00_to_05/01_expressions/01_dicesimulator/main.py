import random

def roll_dice():
    return random.randint(1, 6)

def main():
    for i in range(3):
        dice_1 = roll_dice()
        dice_2 = roll_dice()
        print("-"*50)
        print(f"Roll {i+1}: Dice 1 = {dice_1}, Dice 2 = {dice_2}")

print()

if __name__ == "__main__":
    main()