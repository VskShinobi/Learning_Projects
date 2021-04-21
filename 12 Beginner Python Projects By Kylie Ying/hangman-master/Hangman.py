import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        words = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)
    # print(word_letters)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    # print(used_letters)
    lives = 6


    while len(word_letters) > 0 and lives > 0:

        print('You have', lives,'You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            # print(alphabet - used_letters)
            used_letters.add(user_letter)
            # print(used_letters)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                # print(word_letters)
            else:
                lives = lives - 1
                print(f'\nYour Letter {user_letter} is not in the word.\n')
        elif user_letter in user_letter:
            print('You have already used that letter. Guess another letter.')
        else:
            print("Invalid Character. Please try again")
    if lives == 0:
        print('You died,sorry.The letter was', word)
    else:
        print(f'wow You got the word: {word}')



hangman()