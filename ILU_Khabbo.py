import tkinter as tk
import random
import pygame

# Initialize pygame mixer for music
pygame.mixer.init()

# Load and play background music (replace with your own mp3/wav file)
pygame.mixer.music.load("Sanson Ki Mala Rahat Fateh Ali Khan 128 Kbps.mp3")  # <-- put your music file here
pygame.mixer.music.set_volume(0.5)  # softer volume
pygame.mixer.music.play(-1)  # loop forever

# Create main window
root = tk.Tk()
root.title("Romantic Expression")
root.geometry("600x400")
root.configure(bg="#1c1c1c")

# Fade-in effect for text
def fade_in_text(label, text, delay=100):
    for i, char in enumerate(text):
        root.after(i * delay, lambda c=char: label.config(text=label.cget("text") + c))

# Floating hearts animation
def create_heart():
    x = random.randint(50, 550)
    y = 400
    heart = canvas.create_text(x, y, text="❤", font=("Helvetica", 20), fill="#ff4d6d")
    animate_heart(heart)

def animate_heart(heart):
    def move():
        coords = canvas.coords(heart)
        if coords[1] > -20:
            canvas.move(heart, 0, -2)
            root.after(50, move)
        else:
            canvas.delete(heart)
    move()

# Canvas for hearts
canvas = tk.Canvas(root, width=600, height=400, bg="#1c1c1c", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Romantic label
label = tk.Label(root, text="", font=("Helvetica", 18, "italic"), fg="#ff4d6d", bg="#1c1c1c")
label.place(relx=0.5, rely=0.3, anchor="center")

# Start fade-in text
fade_in_text(label, "Every moment with you feels magical...")

# Generate hearts periodically
def spawn_hearts():
    create_heart()
    root.after(800, spawn_hearts)

spawn_hearts()

root.mainloop()
