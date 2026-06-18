"""
Complete the Word - A simple word-guessing game with a Tkinter GUI.

How to play:
    Run this file with `python word_game.py`. A random word from a
    category is hidden behind blanks. Guess one letter at a time, or
    type the whole word, before you run out of attempts.
"""

import tkinter as tk
from tkinter import messagebox
import random

WORDS = {
    "animal": [
        "elephant", "giraffe", "penguin", "dolphin", "kangaroo", "cheetah",
        "octopus", "flamingo", "hedgehog", "crocodile", "butterfly",
        "chimpanzee", "rhinoceros", "hippopotamus", "woodpecker",
        "jellyfish", "chameleon", "porcupine", "armadillo", "mongoose",
    ],
    "fruit": [
        "banana", "mango", "pineapple", "strawberry", "watermelon",
        "blueberry", "raspberry", "pomegranate", "grapefruit", "kiwi",
        "papaya", "cantaloupe", "blackberry", "tangerine", "nectarine",
        "apricot", "persimmon", "lychee", "durian", "jackfruit",
    ],
    "country": [
        "india", "canada", "brazil", "germany", "japan", "australia",
        "argentina", "portugal", "thailand", "vietnam", "colombia",
        "indonesia", "switzerland", "netherlands", "philippines",
        "singapore", "malaysia", "mexico", "egypt", "kenya",
    ],
    "tech": [
        "python", "computer", "keyboard", "software", "internet",
        "algorithm", "database", "javascript", "processor", "bluetooth",
        "microchip", "smartphone", "encryption", "bandwidth", "debugging",
        "framework", "repository", "blockchain", "cybersecurity",
        "virtualization",
    ],
}

ALL_WORDS = [word for word_list in WORDS.values() for word in word_list]

MAX_ATTEMPTS = 6

BG_COLOR = "#1e2330"
PANEL_COLOR = "#2a3142"
ACCENT_COLOR = "#5cc8ff"
TEXT_COLOR = "#f0f4f8"
WRONG_COLOR = "#ff6b6b"
CORRECT_COLOR = "#6bff95"


class WordGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Complete the Word")
        self.root.geometry("520x460")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        self.category = ""
        self.word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.score = 0
        self.used_words = set()

        self._build_ui()
        self.new_game()

    def _build_ui(self):
        title = tk.Label(
            self.root, text="COMPLETE THE WORD",
            font=("Helvetica", 22, "bold"), bg=BG_COLOR, fg=ACCENT_COLOR,
        )
        title.pack(pady=(20, 5))

        self.score_label = tk.Label(
            self.root, text="Score: 0", font=("Helvetica", 11),
            bg=BG_COLOR, fg=TEXT_COLOR,
        )
        self.score_label.pack()

        panel = tk.Frame(self.root, bg=PANEL_COLOR, padx=20, pady=20)
        panel.pack(pady=15, padx=30, fill="x")

        self.category_label = tk.Label(
            panel, text="", font=("Helvetica", 12, "italic"),
            bg=PANEL_COLOR, fg=ACCENT_COLOR,
        )
        self.category_label.pack()

        self.word_label = tk.Label(
            panel, text="", font=("Courier New", 28, "bold"),
            bg=PANEL_COLOR, fg=TEXT_COLOR,
        )
        self.word_label.pack(pady=15)

        self.guessed_label = tk.Label(
            panel, text="", font=("Helvetica", 10),
            bg=PANEL_COLOR, fg="#9aa5b8",
        )
        self.guessed_label.pack()

        self.attempts_label = tk.Label(
            self.root, text="", font=("Helvetica", 13, "bold"),
            bg=BG_COLOR, fg=TEXT_COLOR,
        )
        self.attempts_label.pack(pady=10)

        entry_frame = tk.Frame(self.root, bg=BG_COLOR)
        entry_frame.pack(pady=10)

        self.entry = tk.Entry(
            entry_frame, font=("Helvetica", 16), width=12, justify="center",
            bg=PANEL_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
            relief="flat",
        )
        self.entry.pack(side=tk.LEFT, padx=8, ipady=6)
        self.entry.bind("<Return>", lambda e: self.guess())

        guess_btn = tk.Button(
            entry_frame, text="Guess", command=self.guess,
            font=("Helvetica", 12, "bold"), bg=ACCENT_COLOR, fg="#1e2330",
            relief="flat", padx=15, pady=5, cursor="hand2",
        )
        guess_btn.pack(side=tk.LEFT)

        self.message_label = tk.Label(
            self.root, text="Guess a letter, or type the whole word and hit Enter.",
            font=("Helvetica", 10), bg=BG_COLOR, fg="#9aa5b8", wraplength=440,
        )
        self.message_label.pack(pady=10)

        new_game_btn = tk.Button(
            self.root, text="New Game", command=self.new_game,
            font=("Helvetica", 11), bg=PANEL_COLOR, fg=TEXT_COLOR,
            relief="flat", padx=12, pady=4, cursor="hand2",
        )
        new_game_btn.pack(pady=(0, 10))

    def new_game(self):
        if len(self.used_words) >= len(ALL_WORDS):
            self.used_words = set()

        available = [w for w in ALL_WORDS if w not in self.used_words]
        self.word = random.choice(available)
        self.used_words.add(self.word)
        self.category = next(cat for cat, words in WORDS.items() if self.word in words)

        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.message_label.config(
            text="Guess a letter, or type the whole word and hit Enter.",
            fg="#9aa5b8",
        )
        self._refresh_display()
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def _refresh_display(self):
        self.category_label.config(text=f"Category: {self.category.upper()}")
        display = "  ".join(
            letter if letter in self.guessed_letters else "_" for letter in self.word
        )
        self.word_label.config(text=display)
        self.attempts_label.config(
            text=f"Attempts left: {MAX_ATTEMPTS - self.wrong_guesses}"
        )
        guessed_text = (
            "Guessed: " + ", ".join(sorted(self.guessed_letters))
            if self.guessed_letters else ""
        )
        self.guessed_label.config(text=guessed_text)
        self.score_label.config(text=f"Score: {self.score}")

    def guess(self):
        text = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)
        if not text:
            return

        if len(text) > 1:
            if text == self.word:
                self._handle_win()
            else:
                self.wrong_guesses += 1
                self.message_label.config(text=f"'{text}' isn't the word.", fg=WRONG_COLOR)
                self._refresh_display()
                self._check_loss()
            return

        if text in self.guessed_letters:
            self.message_label.config(text="Already guessed that letter.", fg="#9aa5b8")
            return

        self.guessed_letters.add(text)

        if text in self.word:
            self.message_label.config(text=f"'{text}' is in the word!", fg=CORRECT_COLOR)
        else:
            self.wrong_guesses += 1
            self.message_label.config(text=f"'{text}' is not in the word.", fg=WRONG_COLOR)

        self._refresh_display()

        if all(letter in self.guessed_letters for letter in self.word):
            self._handle_win()
            return

        self._check_loss()

    def _handle_win(self):
        self.score += 1
        self._refresh_display()
        messagebox.showinfo("You Win!", f"You completed the word: '{self.word}'!")
        self.new_game()

    def _check_loss(self):
        if self.wrong_guesses >= MAX_ATTEMPTS:
            messagebox.showinfo("Game Over", f"Out of attempts! The word was '{self.word}'.")
            self.new_game()


def main():
    root = tk.Tk()
    WordGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
