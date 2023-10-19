import tkinter as tk
import random

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x250")
font = ("Helvetica", 12)

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=font)
instruction_label.pack()

player_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    global player_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Paper" and computer_choice == "Rock") or \
            (user_choice == "Scissors" and computer_choice == "Paper"):
        player_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer's choice: {computer_choice}\n{result}")
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

button_width = 10
button_height = 2
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"), font=font, width=button_width,
                        height=button_height)
paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"), font=font, width=button_width,
                         height=button_height)
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"), font=font, width=button_width,
                            height=button_height)

rock_button.pack()
paper_button.pack()
scissors_button.pack()

result_label = tk.Label(root, text="", font=font)
result_label.pack()

score_label = tk.Label(root, text="Player: 0  Computer: 0", font=font)
score_label.pack()

root.mainloop()
