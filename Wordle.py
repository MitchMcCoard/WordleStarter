# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    
    def enter_action(s):
        s = s.lower()
        
        if s == random_word:
            gw.show_message("Congratulations! You guessed the word correctly!")
        else:
            if s in FIVE_LETTER_WORDS:
                gw.show_message("Smart! Keep at it")
                current_row = gw.get_current_row()
                if current_row < N_ROWS - 1:
                    gw.set_current_row(current_row + 1)
            else:
                gw.show_message("Nope that is not a word")
                current_row = gw.get_current_row()
                gw.set_current_row(current_row)

    gw = WordleGWindow()

    random_word = random.choice(FIVE_LETTER_WORDS)

    for col in range(N_COLS):
        gw.set_square_letter(0,col, random_word[col])
    gw.add_enter_listener(enter_action)

    # def enter_action(s):
    #     gw.show_message("You have to implement this method.")

    # gw = WordleGWindow()
    # gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
