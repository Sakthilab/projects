import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)

length = len(chosen_word)

lives = 6

display = []

for _ in range(length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()    
    os.system('cls')
    if guess in display:
        print(f"you've already guessed {guess}")

    for i in range(length):
        letter = chosen_word[i]
        
        if letter == guess:
            display[i] = letter

    if guess not in chosen_word:
        print(f"you've guessed {guess}, that'ss not in word. you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")    

    if "_" not in display:
        end_of_game = True
        print("you win")

    print(stages[lives])
    

