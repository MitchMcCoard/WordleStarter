# # File: Wordle.py

# import random

# from WordleDictionary import FIVE_LETTER_WORDS
# from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
# from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

# MAX_GUESSES = 6  # Maximum number of guesses

# def wordle():

#     def enter_action(s):
#         s = s.lower()
        
#         if s == random_word:
#             gw.show_message("Congratulations! You guessed the word correctly!\nPress Esc to exit.")
#             for col in range(N_COLS):
#                 current_row = gw.get_current_row()
#                 gw.set_square_color(current_row, col, CORRECT_COLOR)

#                 # Disable further input and end the game
#                 gw._root.unbind("<Key>")
#         else:
#             if s in FIVE_LETTER_WORDS:
#                 current_row = gw.get_current_row()
                
#                 if current_row < N_ROWS:
#                     # Get the randomly chosen word
#                     target_word = list(random_word)

#                     # Initialize lists to track correctness
#                     correct_letters = []
#                     present_letters = []

#                     # Check each letter in the guess
#                     for col in range(N_COLS):
#                         guess_letter = s[col]
#                         target_letter = target_word[col]

#                         if guess_letter == target_letter:
#                             correct_letters.append(col)
#                             target_word[col] = ''  # Mark as used

#                     # Now, check for present but misplaced letters
#                     for col in range(N_COLS):
#                         guess_letter = s[col]
#                         if guess_letter and guess_letter in target_word:
#                             present_letters.append(col)
#                             target_word[target_word.index(guess_letter)] = ''  # Mark as used

#                     # Update square colors based on correctness
#                     for col in range(N_COLS):
#                         if col in correct_letters:
#                             gw.set_square_color(current_row, col, CORRECT_COLOR)
#                         elif col in present_letters:
#                             gw.set_square_color(current_row, col, PRESENT_COLOR)
#                         else:
#                             gw.set_square_color(current_row, col, MISSING_COLOR)
#                     # Check if the player is out of guesses
#                     if current_row == MAX_GUESSES - 1:
#                             gw.show_message(f"Out of guesses! The word was: {random_word} \nPress Esc to exit.")
#                     # Advance to the next row
#                     if current_row < N_ROWS - 1:
#                         gw.set_current_row(current_row + 1)
#             else:
#                 gw.show_message("Nope, that is not a word")
#                 current_row = gw.get_current_row()
#                 gw.set_current_row(current_row)
#     gw = WordleGWindow()

#     random_word = random.choice(FIVE_LETTER_WORDS)
#     #Show Answer in first row
#     # for col in range(N_COLS):
#     #     gw.set_square_letter(0, col, random_word[col])
#     gw.add_enter_listener(enter_action)

#      # Allow the player to exit the game by pressing Esc
#     gw._root.bind("<Escape>", lambda event: gw._root.destroy())

# # Startup code

# if __name__ == "__main__":
#     wordle()


##Tanner's Code
import random
import tkinter as tk
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
MAX_GUESSES = 6  # Maximum number of guesses
def theme_dialog():
    def start_game():
        theme = theme_var.get()
        dialog.destroy()
        wordle(theme)
    dialog = tk.Toplevel()
    dialog.title("Color Selection")
    dialog.geometry("500x700")
    # Theme Selection
    theme_label = tk.Label(dialog, text="Select Theme:")
    theme_label.pack()
    theme_var = tk.StringVar()
    theme_var.set("Light")  # normal mode
    theme_options = ["Light", "Fun"]
    theme_menu = tk.OptionMenu(dialog, theme_var, *theme_options)
    theme_menu.pack()
    # Start Button
    start_button = tk.Button(dialog, text="Start Game", command=start_game)
    start_button.pack()
    dialog.mainloop()
def wordle(theme):
    random_word = random.choice(FIVE_LETTER_WORDS)
    print(random_word)
    if theme == "Light":
        CORRECT_COLOR = "#66BB66" # Light green for correct letters
        PRESENT_COLOR = "#CCBB66" # Brownish yellow for misplaced letters
        MISSING_COLOR = "#999999" # Gray for letters that don’t appear
    elif theme == "Fun":
        # Use the alternate color scheme (define your alternate colors here)
        CORRECT_COLOR = "#39FF14" #neon green
        PRESENT_COLOR = "#F535AA" #neon pink
        MISSING_COLOR = "#00D8FF" #neon blue
    gw = WordleGWindow()
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
    # gw = WordleGWindow()
    # random_word = random.choice(FIVE_LETTER_WORDS)
    #Show Answer in first row
    # for col in range(N_COLS):
    #     gw.set_square_letter(0, col, random_word[col])
    gw.add_enter_listener(enter_action)
     # Allow the player to exit the game by pressing Esc
    gw._root.bind("<Escape>", lambda event: gw._root.destroy())
# Startup code
if __name__ == "__main__":
    theme_dialog()