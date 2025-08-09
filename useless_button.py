import tkinter as tk
import random

def move_button():
    x = random.randint(0, root.winfo_width() - 100)
    y = random.randint(0, root.winfo_height() - 40)
    prank_button.place(x=x, y=y)
    click_counter[0] += 1
    if click_counter[0] >= 10 and click_counter[0]<20:
        prank_button.config(text="Okay, you win 😂")
    if click_counter[0]>=20 and click_counter[0]<25:
        prank_button.config(text="Damn, you are persistent")
    if click_counter[0]>=25 and click_counter[0]<30:
        prank_button.config(text="GET A LIFE, LOSER!!")
        prank_button.quit()
    

root = tk.Tk()
root.title("Useless Button")
root.geometry("400x300")

click_counter = [0]
prank_button = tk.Button(root, text="Click Me!", command=move_button)
prank_button.place(x=150, y=130)

root.mainloop()
