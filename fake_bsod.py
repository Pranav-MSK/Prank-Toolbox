import tkinter as tk

def close_bsod(event):
    root.destroy()

root = tk.Tk()
root.title("😱")
root.attributes("-fullscreen", True)
root.configure(bg="#0000aa")

bsod_text = """
Your PC ran into a problem and needs to restart.
We're just collecting some error info, and then we'll restart for you.

For more information about this issue and possible fixes, visit
https://www.microsoft.com/stopcode

Error Code: PRANK_KERNEL_ERROR
"""

label = tk.Label(root, text=bsod_text, font=("Consolas", 16), bg="#0000aa", fg="white", justify="left")
label.pack(padx=50, pady=100)

root.bind("<Key>", close_bsod)

root.mainloop()
