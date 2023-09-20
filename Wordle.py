# File: Wordle.py

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

MAX_GUESSES = 6  # Maximum number of guesses

def wordle():

    def enter_action(s):
        s = s.lower()
        
        if s == random_word:
            gw.show_message("Congratulations! You guessed the word correctly!\nPress Esc to exit.")
            for col in range(N_COLS):
                current_row = gw.get_current_row()
                gw.set_square_color(current_row, col, CORRECT_COLOR)

                # Disable further input and end the game
                gw._root.unbind("<Key>")
        else:
            if s in FIVE_LETTER_WORDS:
                current_row = gw.get_current_row()
                
                if current_row < N_ROWS:
                    # Get the randomly chosen word
                    target_word = list(random_word)

                    # Initialize lists to track correctness
                    correct_letters = []
                    present_letters = []

                    # Check each letter in the guess
                    for col in range(N_COLS):
                        guess_letter = s[col]
                        target_letter = target_word[col]

                        if guess_letter == target_letter:
                            correct_letters.append(col)
                            target_word[col] = ''  # Mark as used

                    # Now, check for present but misplaced letters
                    for col in range(N_COLS):
                        guess_letter = s[col]
                        if guess_letter and guess_letter in target_word:
                            present_letters.append(col)
                            target_word[target_word.index(guess_letter)] = ''  # Mark as used

                    # Update square colors based on correctness
                    for col in range(N_COLS):
                        if col in correct_letters:
                            gw.set_square_color(current_row, col, CORRECT_COLOR)
                        elif col in present_letters:
                            gw.set_square_color(current_row, col, PRESENT_COLOR)
                        else:
                            gw.set_square_color(current_row, col, MISSING_COLOR)
                    # Check if the player is out of guesses
                    if current_row == MAX_GUESSES - 1:
                            gw.show_message(f"Out of guesses! The word was: {random_word} \nPress Esc to exit.")
                    # Advance to the next row
                    if current_row < N_ROWS - 1:
                        gw.set_current_row(current_row + 1)
            else:
                gw.show_message("Nope, that is not a word")
                current_row = gw.get_current_row()
                gw.set_current_row(current_row)
    gw = WordleGWindow()

    random_word = random.choice(FIVE_LETTER_WORDS)
    #Show Answer in first row
    # for col in range(N_COLS):
    #     gw.set_square_letter(0, col, random_word[col])
    gw.add_enter_listener(enter_action)

     # Allow the player to exit the game by pressing Esc
    gw._root.bind("<Escape>", lambda event: gw._root.destroy())

# Startup code

if __name__ == "__main__":
    wordle()
