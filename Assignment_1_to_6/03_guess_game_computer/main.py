low = 1
high = 100
guess = 0
tries = 0
print("-"*50)
print("Welcome to guess game")
print("-"*50)
print("Think a number between 1 - 100")
input("When you are ready press 'Enter' ")
while True:
  tries += 1
  guess = (low + high) // 2
  user = input(f"\nMy Guess is {guess} is my Guess 'Higher' or 'Lower'? \nEnter l for 'low' h for 'high' c for correct: ")
  if user == "l":
    low = guess + 1
  elif user == "h":
    high = guess - 1
  elif user == "c":
    print("-"* 50)
    print(f"Hurahhh! i guess the correct number {guess} in {tries} tries\n")
    break
  
