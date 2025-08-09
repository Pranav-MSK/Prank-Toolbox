import tkinter as tk
import time
from threading import Thread

def fake_update():
    for i in range(100):
        time.sleep(0.05 if i < 98 else 1.5)
        progress["value"] = i + 1
        text_var.set(f"Installing Updates... {i+1}%")
        root.update_idletasks()
    text_var.set("Installing prankware.exe 🤡")

root = tk.Tk()
root.title("Windows Update")
root.geometry("500x200")
root.resizable(False, False)
root.configure(bg="black")

text_var = tk.StringVar(value="Installing Updates... 0%")
tk.Label(root, textvariable=text_var, font=("Segoe UI", 16), bg="black", fg="white").pack(pady=30)

from tkinter.ttk import Progressbar
progress = Progressbar(root, length=400, mode='determinate')
progress.pack()

Thread(target=fake_update).start()

root.mainloop()
