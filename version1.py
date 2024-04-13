import tkinter as tk
import random
from tkinter import simpledialog, messagebox

# Define sports theme word list with hints
sports_words_with_hints = {
    "soccer": "A game played between two teams of eleven players with a spherical ball.",
    "basketball": "A game played between two teams of five players with a hoop and a ball.",
    "tennis": "A game played between two or four players with rackets and a ball.",
    "volleyball": "A game played between two teams with a ball over a high net.",
    "cricket": "A game played with a bat and ball between two teams of eleven players.",
    "baseball": "A game played between two teams with a bat and a ball on a diamond-shaped field.",
    "golf": "A game played on a course with a series of holes in which players hit a ball into each hole with the fewest strokes.",
    "swimming": "A sport in which individuals or teams race to swim across a pool or in open water.",
    "boxing": "A combat sport in which two people fight using their fists.",
    "athletics": "A collection of sports events including running, jumping, throwing, and walking."
}

# Define ASCII art for hangman
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

# Choose a random word from the sports theme with its hint
word, hint = random.choice(list(sports_words_with_hints.items()))
word = word.lower()  # Convert word to lowercase
word_with_blanks = ['_'] * len(word)

# Function to update hangman ASCII art
def update_hangman(mistake):
    max_mistake_index = min(len(hangman_art) - 1, mistake)
    hangman_label.config(text=hangman_art[max_mistake_index])

# Function to check guessed letter
def check_guess(letter):
    global guesses_left
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                word_with_blanks[i] = letter
        word_label.config(text=' '.join(word_with_blanks))
        if '_' not in word_with_blanks:
            end_game("win")
    else:
        guesses_left -= 1
        update_hangman(6 - guesses_left)
        if guesses_left == 0:
            end_game("lose")
    disable_alphabet_button(letter)

# Function to disable alphabet button after it's clicked
def disable_alphabet_button(letter):
    alphabet_buttons[ord(letter) - ord('a')].config(state=tk.DISABLED)

# Function to end the game
def end_game(result):
    if result == "win":
        result_text = "You win!"
    else:
        result_text = "You Lose, the word was " + word
    result_label.config(text=result_text)
    restart_button.pack()  # Display the restart button

# Function to restart the game
def restart_game():
    global word, hint, word_with_blanks, guesses_left
    word, hint = random.choice(list(sports_words_with_hints.items()))
    word = word.lower()
    word_with_blanks = ['_'] * len(word)
    word_label.config(text=' '.join(word_with_blanks))
    guesses_left = 6
    update_hangman(0)
    result_label.config(text="")
    hint_label.config(text=f"Hint: {hint}")  # Update hint label
    for button in alphabet_buttons:
        button.config(state="normal")
    restart_button.pack_forget()  # Hide the restart button

root = tk.Tk()
root.title("Hangman Game")

# Set initial size of the window
root.geometry("600x400")

hangman_label = tk.Label(root, font=("Courier", 36))
hangman_label.pack()

word_label = tk.Label(root, text='', font=("Arial", 24))
word_label.pack()

result_label = tk.Label(root, font=("Arial", 24))
result_label.pack()

hint_label = tk.Label(root, font=("Arial", 15), wraplength=400)
hint_label.pack()

alphabet_frame = tk.Frame(root)
alphabet_frame.pack()

alphabet_buttons = []
for i in range(26):
    letter = chr(ord('a') + i)
    button = tk.Button(alphabet_frame, text=letter, font=("Arial", 14), command=lambda l=letter: check_guess(l))
    button.grid(row=i // 7, column=i % 7, padx=5, pady=5)
    alphabet_buttons.append(button)

guesses_left = 6
update_hangman(0)

restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.pack()
restart_button.pack_forget()  # Initially hide the restart button

# Call restart_game() initially to set up the game
restart_game()

# Start the event loop
root.mainloop()