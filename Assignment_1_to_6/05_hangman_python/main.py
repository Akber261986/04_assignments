import random
from word_list import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in words or ' ' in words:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()


    while len(word_letters) > 0:
        print("you have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word: ", " ".join(word_list))
        user_letters = input('Guess a letter: ').upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
        elif user_letters in used_letters:
            print("You have already used that chracter, please try again. ")
        else:
            print("Invalid chracter, please try again. ")
    print("You Guess the correct word", word, '!!')

hangman()