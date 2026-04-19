import tkinter as tk
import random
import pygame

# Initialize pygame mixer for music
pygame.mixer.init()

# Load and play background music (replace with your own mp3/wav file)
pygame.mixer.music.load("SansonKiMala.mp3")  # <-- put your music file here
pygame.mixer.music.set_volume(0.5)  # softer volume
pygame.mixer.music.play(-1)  # loop forever

# Create main window
root = tk.Tk()
root.title("I Still Love You Khabbo")
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
fade_in_text(label, "Every moment with you feels magical,My dearest Shafaq, Meri Pyaari Khabbo, It has been four long months since your voice last touched my soul, and every day without you has felt like a lifetime of silence. I find myself reaching for you in the quiet of the night, whispering your name into the emptiness, hoping somehow it will reach you. I know I have made mistakes, and I know distance has grown between us, but my heart has never stopped beating for you. Every memory of your laughter, every glance of your eyes, every word you once spoke to me still lives inside me like a flame that refuses to die.Khabbo, you are not just a part of my life—you are my life. Without you, the colors fade, the music stops, and the world feels unbearably heavy. I ache for the warmth of your presence, for the chance to hold your hand again and promise you that I will never let go. Please, Shafaq, let me back into your world. Let me prove that my love for you is stronger than time, stronger than silence, stronger than the mistakes that kept us apart. I am ready to fight for us, to cherish you, to protect the fragile beauty of what we share. You are my home, my peace, my forever. Accept me once more, and I will spend every breath showing you that you are the only one my heart will ever belong to.")

# Generate hearts periodically
def spawn_hearts():
    create_heart()
    root.after(800, spawn_hearts)

spawn_hearts()

root.mainloop()
