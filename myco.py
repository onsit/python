import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Love Note for My Sweetheart")
window.geometry("400x300")  # Set window size
window.configure(bg="#ffe6f0")  # Light pink background

# Function to show a pop-up message
def show_love_message():
    messagebox.showinfo("For You", "You’re the cutest person in the world, and I’m so lucky to have you! 💕")

# Add a cute title label
title_label = tk.Label(
    window,
    text="To My Darling",
    font=("Comic Sans MS", 20, "bold"),
    bg="#ffe6f0",
    fg="#ff6699"  # Soft pinkish-red text
)
title_label.pack(pady=20)

# Add a heart symbol (you can use emoji or text)
heart_label = tk.Label(
    window,
    text="♥",
    font=("Arial", 40),
    bg="#ffe6f0",
    fg="#ff3366"  # Bright pink heart
)
heart_label.pack()

# Add a sweet message
message_label = tk.Label(
    window,
    text="You make my heart skip a beat every day!",
    font=("Comic Sans MS", 12),
    bg="#ffe6f0",
    fg="#ff6699",
    wraplength=350
)
message_label.pack(pady=10)
