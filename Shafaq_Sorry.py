import tkinter as tk
import random
import pygame

# Initialize pygame mixer for music
pygame.mixer.init()

# Load and play background music (replace with your own mp3/wav file)
pygame.mixer.music.load("SansonKiMala.mp3")  # <-- your first music file
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Create main window
root = tk.Tk()
root.title("Romantic Expression for Shafaq")
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

# Second button: personalized message for Shafaq (Khabbo)
def special_message():
    pygame.mixer.music.load("KaliKaliZulfon.mp3")  # <-- another music file
    pygame.mixer.music.play(-1)
    label.config(text="Shafaq, Meri Khabbo... You are my forever.")

btn1 = tk.Button(root, text="Click to know my heart",
                 font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#333333",
                 activebackground="#ff4d6d", command=lambda: label.config(text="My Dearest Shafaq, from the very first moment we became friends, you brought light into my life. Every laugh we’ve shared, every conversation we’ve had, has made me realize how precious you are to me. You are not just my best friend—you are my safe place, my joy, and the person who makes even ordinary days feel extraordinary. I cherish the bond we share, and I find myself dreaming of a future where we walk side by side, not just as friends, but as partners in life. I call you “Khabbo” because that name carries all the affection and tenderness I feel for you. It’s my way of holding you close, even when words fall short. I don’t know what tomorrow holds, but I do know this: my heart feels complete when I think of you. You are my everything, and I cannot imagine my world without your presence in it.With all my love, You are my everything, Shafaq."))
btn1.place(relx=0.5, rely=0.6, anchor="center")

btn2 = tk.Button(root, text="Specially for you, Meri Khabbo",
                 font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#444444",
                 activebackground="#ff4d6d", command=special_message)
btn2.place(relx=0.5, rely=0.75, anchor="center")

root.mainloop()
