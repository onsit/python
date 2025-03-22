import tkinter as tk
from tkinter import ttk
import random

# Create the main window
window = tk.Tk()
window.title("Love Dashboard for My Baby")
window.geometry("500x400")
window.configure(bg="#fff0f5")  # Soft pastel pink

# Canvas for animation
canvas = tk.Canvas(window, width=300, height=150, bg="#fff0f5", highlightthickness=0)
canvas.pack(pady=20)

# Bouncing heart animation
heart = canvas.create_text(150, 75, text="♥", font=("Arial", 50), fill="#ff3366")
heart_x, heart_y = 150, 75
heart_dy = 3  # Vertical speed

def animate_heart():
    global heart_y, heart_dy
    canvas.move(heart, 0, heart_dy)
    heart_y += heart_dy
    if heart_y > 120 or heart_y < 30:  # Bounce between top and bottom
        heart_dy = -heart_dy
    window.after(50, animate_heart)  # Repeat every 50ms

# Start animation
animate_heart()

# Frame for content
frame = ttk.Frame(window, padding=10)
frame.pack()

# Cute title
title_label = ttk.Label(
    frame,
    text="My Love Dashboard",
    font=("Comic Sans MS", 18, "bold"),
    foreground="#ff6699"
)
title_label.pack(pady=10)

# Compliment generator
compliments = [
    "You’re sweeter than a cupcake!",
    "Your smile lights up my world!",
    "You’re my favorite person ever!",
    "You make every day magical!",
    "You’re cuter than a basket of kittens!"
]

def generate_compliment():
    compliment_text.set(random.choice(compliments))

compliment_text = tk.StringVar()
compliment_text.set("Click for a compliment!")
compliment_label = ttk.Label(
    frame,
    textvariable=compliment_text,
    font=("Comic Sans MS", 12),
    foreground="#ff6699"
)
compliment_label.pack(pady=5)

compliment_button = ttk.Button(
    frame,
    text="Get a Compliment!",
    command=generate_compliment
)
compliment_button.pack(pady=5)

# Love meter (progress bar)
love_label = ttk.Label(
    frame,
    text="How Much I Love You:",
    font=("Comic Sans MS", 12),
    foreground="#ff6699"
)
love_label.pack(pady=5)

love_meter = ttk.Progressbar(
    frame,
    length=200,
    mode="determinate",
    maximum=100
)
love_meter.pack()
love_meter["value"] = 100  # It’s always 100% for her!

# Secret message button
def secret_message():
    tk.messagebox.showinfo("Secret Note", "I’d cross the universe just to see you smile! 💕")

secret_button = ttk.Button(
    frame,
    text="Secret Love Note",
    command=secret_message
)
secret_button.pack(pady=10)

# Style the buttons and labels
style = ttk.Style()
style.configure("TButton", font=("Comic Sans MS", 10), background="#ff99cc", foreground="white")
style.configure("TLabel", background="#fff0f5")

# Run the app
window.mainloop()