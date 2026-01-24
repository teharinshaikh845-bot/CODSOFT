import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- Password Logic (Backend) ----------------
def generate_password():
    length = length_var.get()

    if length < 4:
        messagebox.showwarning("Warning", "Password length should be at least 4")
        return

    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase
    if lower_var.get():
        characters += string.ascii_lowercase
    if number_var.get():
        characters += string.digits
    if symbol_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Please select at least one option")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# ---------------- Copy Function ----------------
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- GUI (Frontend) ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("420x400")
root.config(bg="#f2f2f2")

tk.Label(root, text="🔐 Password Generator", font=("Arial", 18, "bold"), bg="#f2f2f2").pack(pady=10)

# Length
length_var = tk.IntVar(value=8)
tk.Label(root, text="Password Length:", font=("Arial", 11), bg="#f2f2f2").pack()
tk.Spinbox(root, from_=4, to=32, textvariable=length_var, width=5).pack(pady=5)

# Options
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
number_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, bg="#f2f2f2").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, bg="#f2f2f2").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Numbers", variable=number_var, bg="#f2f2f2").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var, bg="#f2f2f2").pack(anchor="w", padx=60)

# Generate Button
tk.Button(root, text="Generate Password", font=("Arial", 11, "bold"),
          bg="#4CAF50", fg="white", command=generate_password).pack(pady=15)

# Result
result_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=30)
result_entry.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy Password", bg="#2196F3", fg="white",
          command=copy_password).pack(pady=10)

# Footer
tk.Label(root, text="Python Programming Internship Project",
         font=("Arial", 9), bg="#f2f2f2", fg="gray").pack(side="bottom", pady=10)

root.mainloop()
