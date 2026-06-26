import tkinter as tk
from tkinter import messagebox
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    messagebox.showinfo(
        "Result",
        f"Your Choice: {user_choice}\n"
        f"Computer Choice: {computer_choice}\n\n"
        f"{result}"
    )

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x250")

title = tk.Label(root, text="Rock Paper Scissors Game",
                 font=("Arial", 16, "bold"))
title.pack(pady=20)

tk.Button(root, text="Rock", width=15,
          command=lambda: play("Rock")).pack(pady=5)

tk.Button(root, text="Paper", width=15,
          command=lambda: play("Paper")).pack(pady=5)

tk.Button(root, text="Scissors", width=15,
          command=lambda: play("Scissors")).pack(pady=5)

root.mainloop()