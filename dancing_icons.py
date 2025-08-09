import tkinter as tk
import random

icons = ["📁", "🗑️", "📄", "🖼️", "📊", "🎵", "🎮", "🧪"]

def animate():
    for label in icon_labels:
        x = random.randint(0, 500)
        y = random.randint(0, 400)
        label.place(x=x, y=y)
    root.after(300, animate)

root = tk.Tk()
root.title("Desktop Icons")
root.geometry("600x450")
root.configure(bg="#004")

tk.Label(root, text="Dancing Icons 🕺", font=("Arial", 20), bg="#004", fg="white").pack()

icon_labels = []
for i in range(10):
    emoji = random.choice(icons)
    lbl = tk.Label(root, text=emoji, font=("Arial", 24), bg="#004", fg="white")
    lbl.place(x=random.randint(0, 500), y=random.randint(0, 400))
    icon_labels.append(lbl)

animate()

root.mainloop()
