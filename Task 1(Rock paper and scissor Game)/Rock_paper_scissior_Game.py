import tkinter as tk
import random

win = tk.Tk()
win.title("RPS Game")
win.geometry("380x300")

choices = ["Rock", "Paper", "Scissors"]
colors = ["#0d64bb", "#1908b0", "#02C148"]
score = [0, 0]  # Player, Computer

tk.Label(win, text="Rock Paper Scissors", font=("Arial", 14, "bold")).pack(pady=10)
result = tk.Label(win, font=("Arial", 12))
result.pack(pady=5)

score_label = tk.Label(win, text=f"Player: {score[0]}  Computer: {score[1]}", font=("Arial", 11))
score_label.pack()

def play(choice):
    comp = random.choice(choices)
    if choice == comp:
        result.config(text=f"Draw! Both chose {choice}", fg="blue")
    elif (choice == "Rock" and comp == "Scissors") or \
         (choice == "Paper" and comp == "Rock") or \
         (choice == "Scissors" and comp == "Paper"):
        score[0] += 1
        result.config(text=f"You Win! Computer chose {comp}", fg="green")
    else:
        score[1] += 1
        result.config(text=f"You Lose! Computer chose {comp}", fg="red")
    score_label.config(text=f"Player: {score[0]}  Computer: {score[1]}")

# Game Buttons
btn_frame = tk.Frame(win)
btn_frame.pack(pady=10)
for i, choice in enumerate(choices):
    tk.Button(btn_frame, text=choice, width=10, font=("Arial", 10),
              bg=colors[i], fg="white", command=lambda c=choice: play(c)).grid(row=0, column=i, padx=5)

# Quit Button
def show_final_score():
    print(f"Final Score - Player: {score[0]}, Computer: {score[1]}")
    win.quit()

tk.Button(win, text="Quit", width=8, font=("Arial", 10),
          bg="#b82110", fg="white", command=show_final_score).pack(pady=15)

win.mainloop()