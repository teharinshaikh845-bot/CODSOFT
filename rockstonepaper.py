import tkinter as tk
import random

# ---------------- Game Logic (Backend) ----------------
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text=f"Your Choice: {user_choice}")
    comp_label.config(text=f"Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Score ➜ You: {user_score} | Computer: {computer_score}")

# ---------------- GUI (Frontend) ----------------
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("450x420")
root.config(bg="#f5f5f5")

tk.Label(root, text="🎮 Rock Paper Scissors",
         font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=10)

tk.Label(root, text="Choose one:",
         font=("Arial", 12), bg="#f5f5f5").pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock ✊", width=10, bg="#FF7043",
          fg="white", command=lambda: play("Rock")).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="Paper ✋", width=10, bg="#42A5F5",
          fg="white", command=lambda: play("Paper")).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="Scissors ✌", width=10, bg="#66BB6A",
          fg="white", command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Display Labels
user_label = tk.Label(root, text="Your Choice: ",
                      font=("Arial", 11), bg="#f5f5f5")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer Choice: ",
                      font=("Arial", 11), bg="#f5f5f5")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ",
                        font=("Arial", 14, "bold"), fg="purple", bg="#f5f5f5")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score ➜ You: 0 | Computer: 0",
                       font=("Arial", 12), bg="#f5f5f5")
score_label.pack(pady=10)

# Footer
tk.Label(root, text="Python Programming Internship Project",
         font=("Arial", 9), fg="gray", bg="#f5f5f5").pack(side="bottom", pady=10)

root.mainloop()
