import tkinter as tk
from tkinter import messagebox
import random

def play(choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    if choice == computer_choice:
        result.set(f"It's a tie! Computer also chose {computer_choice}.")
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "scissors" and computer_choice == "paper") or \
         (choice == "paper" and computer_choice == "rock"):
        result.set(f"You win! Computer chose {computer_choice}.")
        user_score += 1
    else:
        result.set(f"You lose! Computer chose {computer_choice}.")
        computer_score += 1

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def quit_game():
    if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

result = tk.StringVar()
result.set("Choose rock, paper, or scissors to play!")

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

result_label = tk.Label(root, textvariable=result, font=("Arial", 14), wraplength=350)
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

score_frame = tk.Frame(root)
score_frame.pack(pady=20)

user_score_label = tk.Label(score_frame, text="Your Score: 0", font=("Arial", 12))
user_score_label.grid(row=0, column=0, padx=20)

computer_score_label = tk.Label(score_frame, text="Computer Score: 0", font=("Arial", 12))
computer_score_label.grid(row=0, column=1, padx=20)

quit_button = tk.Button(root, text="Quit", font=("Arial", 12), command=quit_game)
quit_button.pack(pady=10)

root.mainloop()
