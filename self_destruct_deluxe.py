import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
import threading
import random
import os
import sys
from playsound import playsound

class SelfDestructApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💣 Self-Destruct Deluxe")
        self.root.geometry("600x400")
        self.root.configure(bg="#0a0a0a")
        self.root.resizable(False, False)
        self.pulsing_active = True

        self.status_text = tk.StringVar()
        self.status_text.set("⚠️ WARNING: Do NOT press the red button!")

        # Optional background image (use your own path)
        try:
            bg_image = tk.PhotoImage(file=self.get_resource_path("assets/background.png"))
            bg_label = tk.Label(root, image=bg_image)
            bg_label.place(relwidth=1, relheight=1)
            bg_label.lower()
            self.bg_image = bg_image
        except:
            pass  # ignore if image not found

        self.label = tk.Label(
            root,
            textvariable=self.status_text,
            font=("Courier New", 16, "bold"),
            fg="#ff5555",
            bg="#0a0a0a",
            wraplength=550,
            justify="center"
        )
        self.label.pack(pady=30)

        self.button = tk.Button(
            root,
            text="💀 INITIATE SELF-DESTRUCT 💀",
            font=("Courier New", 18, "bold"),
            bg="red",
            fg="white",
            activebackground="#8b0000",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            command=self.start_self_destruct
        )
        self.button.pack(pady=10)

        # Progress bar for fake loading
        style = Style()
        style.theme_use('clam')
        style.configure("TProgressbar", thickness=20, troughcolor="#222", background="#ff2222")
        self.progress = Progressbar(root, style="TProgressbar", length=400, mode='determinate')
        self.progress.pack(pady=10)
        self.progress.pack_forget()

        self.pulse_state = 0
        self.pulse_button()

        self.funny_messages = [
            "Initiating self-destruct sequence...",
            "Overloading memory banks...",
            "Injecting JavaScript into the fridge...",
            "Uploading consciousness to ChatGPT...",
            "Wiping hard drive (99%)...",
            "Encrypting files with quantum banana...",
            "Just kidding. Maybe.",
        ]

        self.error_messages = [
            "ERROR 404: Common Sense Not Found",
            "Fatal Error: Sandwich Not Found",
            "Crash.exe has crashed",
            "Crash Imminent: Save your Brains",
            "Warning: Your computer is too cool to crash",
            "System Integrity = LOL",
        ]

        self.explosion_sound_path = self.get_resource_path("assets/boom.wav")
        self.root.after(500, self.start_self_destruct)  # starts after 1 second

    def get_resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def play_sound(self):
        try:
            playsound(self.explosion_sound_path)
        except Exception as e:
            # fallback: small beep if playsound fails (platform dependent)
            try:
                import winsound
                winsound.Beep(800, 300)
            except Exception:
                print(f"[Warning] Failed to play sound: {e}")

    def flash_screen(self, count=0):
        if count >= 6:
            return
        new_color = "#8b0000" if self.root["bg"] == "#0a0a0a" else "#0a0a0a"
        self.root.configure(bg=new_color)
        self.label.configure(bg=new_color)
        self.root.after(200, self.flash_screen, count + 1)

    def fake_errors(self, remaining=2):
        if remaining <= 0:
            return
        messagebox.showerror("💥 CRITICAL ERROR 💥", random.choice(self.error_messages))
        delay = random.randint(1500, 3000)
        self.root.after(delay, self.fake_errors, remaining - 1)

    def start_self_destruct(self):
        self.button.config(state="disabled")
        threading.Thread(target=self.self_destruct_sequence).start()

    def self_destruct_sequence(self):
        for msg in self.funny_messages:
            glitched = self.glitch_text(msg)
            self.status_text.set(glitched)
            self.root.update()
            threading.Event().wait(random.uniform(1.2, 2))

        # start fake errors in parallel and begin fake loading
        self.root.after(0, self.fake_errors)
        self.root.after(0, self.start_fake_loading)

    def countdown(self, i):
        if i <= 0:
            self.trigger_boom()
            return

        # update status
        self.status_text.set(f"Self-destruct in {i}...")

        # final 3 seconds: progressively more chaos
        if i <= 3:
            self.flash_screen()
            self.shake_window()
            # progressive popups: 3 -> 6 -> 12
            popup_counts = {3: 3, 2: 6, 1: 12}
            count = popup_counts.get(i, 3)
            for _ in range(count):
                # spawn non-blocking popups (Toplevel windows)
                self.spawn_fake_error_window()

        self.root.after(1000, self.countdown, i - 1)

    def trigger_boom(self):
        # show BOOM, play sound, then enter attempt recovery -> fail -> blackout sequence cleanly
        self.root.configure(bg="#0a0a0a")
        self.status_text.set("💥 BOOM! 💥")

        # big BOOM label
        boom_label = tk.Label(
            self.root,
            text="💥 BOOM! 💥",
            font=("Courier New", 40, "bold"),
            fg="red",
            bg="#0a0a0a"
        )
        boom_label.pack(pady=20)
        self.root.update()

        # play explosion sound on a thread
        threading.Thread(target=self.play_sound).start()

        # After short pause, start recovery attempt sequence (no blocking dialogs)
        self.root.after(1200, self.attempt_recovery_sequence)

    def attempt_recovery_sequence(self):
        # show a temporary "Attempting recovery..." with animated dots for drama
        attempting_var = tk.StringVar()
        attempting_var.set("Attempting recovery")

        attempting_label = tk.Label(
            self.root,
            textvariable=attempting_var,
            font=("Courier New", 20, "bold"),
            fg="#ff8800",
            bg="#0a0a0a",
            justify="center"
        )
        # put it under the BOOM label (or center if BOOM removed)
        attempting_label.pack(pady=10)

        # animate dots for ~3.5 seconds, then show failure
        start_time_ms = 0
        dot_state = {"dots": 0, "elapsed": 0}

        def animate_dots():
            dot_state["dots"] = (dot_state["dots"] + 1) % 4
            dots = "." * dot_state["dots"]
            attempting_var.set(f"Attempting recovery{dots}")
            dot_state["elapsed"] += 300
            if dot_state["elapsed"] < 3500:
                self.root.after(300, animate_dots)
            else:
                # remove attempting label and show recovery failed
                attempting_label.destroy()
                self.show_system_recovery_failed()

        animate_dots()

    def show_system_recovery_failed(self):
        self.pulsing_active = False
        # Clear the window widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="black")

        # Create label but start it dark, then "fade in" by increasing brightness
        fail_label = tk.Label(
            self.root,
            text="System Recovery Failed.\nPlease contact your administrator.\n\n💀",
            font=("Courier New", 22, "bold"),
            fg="#200000",  # start very dark red
            bg="black",
            justify="center"
        )
        fail_label.pack(expand=True)

        # Simulated fade-in: step the color from dark to bright red
        steps = 10
        def fade(step=0):
            if step > steps:
                # after fully faded, wait a moment then blackout
                self.root.after(2000, self.blackout_screen)
                return
            # interpolate red channel from 0x20 -> 0xFF
            start = 0x20
            end = 0xFF
            val = int(start + (end - start) * (step / steps))
            hex_col = f"#{val:02x}0000"  # red channel only
            fail_label.configure(fg=hex_col)
            self.root.after(120, fade, step + 1)

        fade(0)

    def blackout_screen(self):
        # destroy everything and leave a pure black screen for a moment, then quit
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.configure(bg="black")
        # final delay so user sees the black screen; quit after that
        self.root.after(2500, self.root.quit)

    def start_fake_loading(self):
        self.progress.pack()
        self.progress["value"] = 0
        self.fake_loading()

    def fake_loading(self):
        if self.progress["value"] >= 100:
            self.progress.pack_forget()
            # start countdown after loading completes
            self.countdown(10)
            return
        # bump progress but slow near the end for suspense
        increment = random.randint(5, 15)
        # chance to slow down when nearing 80-95%
        if self.progress["value"] > 70 and random.random() < 0.6:
            increment = random.randint(1, 6)
        self.progress["value"] += increment
        self.root.after(300, self.fake_loading)

    def pulse_button(self):
        if not self.pulsing_active:
            return
        colors = ["#ff0000", "#cc0000", "#990000", "#cc0000"]
        self.button.configure(bg=colors[self.pulse_state % len(colors)])
        self.pulse_state += 1
        self.root.after(500, self.pulse_button)

    def glitch_text(self, msg):
        if random.random() < 0.3:
            # keep spaces but alter characters
            return ''.join(random.choice([c.upper(), c.lower(), '#', '@', '*']) if c != ' ' else ' ' for c in msg)
        return msg

    def shake_window(self):
        def shake():
            x, y = self.root.winfo_x(), self.root.winfo_y()
            for _ in range(8):
                self.root.geometry(f"+{x + random.randint(-10, 10)}+{y + random.randint(-10, 10)}")
                self.root.update()
                self.root.after(30)
            self.root.geometry(f"+{x}+{y}")
        self.root.after(0, shake)

    def spawn_fake_error_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = random.randint(0, max(0, screen_width - 220))
        y = random.randint(0, max(0, screen_height - 120))

        popup = tk.Toplevel(self.root)
        popup.geometry(f"220x120+{x}+{y}")
        popup.configure(bg='black')
        popup.overrideredirect(True)  # Removes window frame

        # Simulate tilt/rotation by offsetting label placement
        label = tk.Label(popup,
                        text=random.choice(self.error_messages),
                        font=("Courier New", 9, "bold"),
                        fg="red",
                        bg="black",
                        wraplength=200,
                        justify="center")
        label.place(x=random.randint(5, 15), y=random.randint(5, 20))

        # Fake OK button
        fake_btn = tk.Button(popup, text="OK", font=("Arial", 9), bg="#330000", fg="white", relief="groove")
        fake_btn.place(x=random.randint(80, 120), y=random.randint(70, 90))

        # Auto-close after a short random time for more chaos
        popup.after(random.randint(1600, 3000), popup.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    # fullscreen - press Esc to exit during testing
    root.attributes("-fullscreen", True)
    root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))
    app = SelfDestructApp(root)
    root.mainloop()
