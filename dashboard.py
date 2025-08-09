import tkinter as tk
import subprocess
import sys
import os
import random
import time
import threading

# List of prank EXEs (same folder as dashboard EXE)
PRANKS = [
    ("💣 Self Destruct PC", "self_destruct_deluxe.exe"),
    ("📟 Infinite Update Simulator", "infinite_update.exe"),
    ("🙃 Useless Button", "useless_button.exe"),
    ("💻 Fake BSOD", "fake_bsod.exe"),
    ("💃 Dancing Icons (Fake)", "dancing_icons.exe")
]

chaos_triggered = False  # Tracks if chaos mode has run
exit_enabled = True      # Controls whether the exit button works

def exe_path(exe_name):
    """Get the full path to an exe (works inside PyInstaller)."""
    if getattr(sys, 'frozen', False):
        # Running from a compiled EXE
        base_path = os.path.dirname(sys.executable)
    else:
        # Running from source (for testing)
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, exe_name)

def launch_prank(exe_name):
    """Launch a prank executable in a separate process."""
    subprocess.Popen([exe_path(exe_name)])

def chaos_mode():
    """Launch random pranks repeatedly for 30 seconds."""
    global exit_enabled
    exit_enabled = False  # Disable exit functionality

    chaos_label = tk.Label(root, text="🔥 CHAOS MODE ACTIVATED 🔥",
                           font=("Courier New", 18, "bold"),
                           fg="red", bg="#111")
    chaos_label.pack(pady=10)

    end_time = time.time() + 30

    def run_chaos():
        while time.time() < end_time:
            prank = random.choice(PRANKS)
            launch_prank(prank[1])
            time.sleep(random.uniform(3, 6))
        chaos_label.config(text="Chaos Mode Complete! You may now exit.")
        # Re-enable exit after chaos
        global exit_enabled
        exit_enabled = True

    threading.Thread(target=run_chaos, daemon=True).start()

def on_exit():
    global chaos_triggered
    if not exit_enabled:
        # Exit button is temporarily disabled
        return
    if not chaos_triggered:
        chaos_triggered = True
        chaos_mode()
    else:
        root.quit()

# -------------------- GUI Setup --------------------
root = tk.Tk()
root.title("🤣 Prank Toolbox 1.0")
root.geometry("500x500")
root.configure(bg="#111")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🎭 Prank Toolbox 🎭",
                       font=("Courier New", 24, "bold"),
                       fg="red", bg="#111")
title_label.pack(pady=20)

# Styling for buttons
def make_button(parent, text, command, bg_color="#333", fg_color="white", hover_color="#555"):
    btn = tk.Button(parent, text=text, font=("Courier New", 14, "bold"),
                    bg=bg_color, fg=fg_color,
                    activebackground=hover_color, activeforeground="white",
                    relief="flat", width=30, pady=8, command=command)
    btn.pack(pady=5)

    def on_enter(e): btn.config(bg=hover_color)
    def on_leave(e): btn.config(bg=bg_color)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# Add prank buttons
for prank_name, exe in PRANKS:
    make_button(root, prank_name, lambda e=exe: launch_prank(e),
                bg_color="#444", hover_color="#666")

# Exit button
exit_btn = tk.Button(root, text="❌ Exit", font=("Courier New", 14, "bold"),
                     bg="#660000", fg="white",
                     activebackground="#aa0000", activeforeground="white",
                     relief="flat", width=20, pady=8, command=on_exit)
exit_btn.pack(side="bottom", pady=20)

root.mainloop()
