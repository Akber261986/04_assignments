import random

def roll_dice():
    return random.randint(1, 6)

def main():
    dice_1 = roll_dice()
    dice_2 = roll_dice()
    print(f"Dice 1 = {dice_1}\nDice 2 = {dice_2}\nSum of both is: {dice_1 + dice_2}")

if __name__ == "__main__":
    main()