# 🎭 Prank Toolbox

**Prank Toolbox** is a collection of light-hearted, fake “chaos” tools written in Python — perfect for harmless fun with friends and co-workers (who have a sense of humor!).  

⚠️ **Disclaimer:** This project is for educational and entertainment purposes only. All pranks are completely safe — they do not cause permanent damage to your system — but always get permission before running them on someone else’s computer.

---

## ✨ Features

- 🖥 **Self Destruct Deluxe** – Fake self-destruct countdown with warning sounds, pop-ups, flashing screen, and “System Recovery Failed” finale.
- ⏳ **Infinite Update Simulator** – Pretends your computer is “updating” forever.
- 🔘 **Useless Button** – A button that just refuses to be useful.
- 💻 **Fake BSOD** – Simulates a full-screen Windows blue screen of death.
- 💃 **Dancing Icons** – Random icons move around your desktop.
- 🎯 **Dashboard Launcher** – A central menu to select and launch any prank.
- 😈 **Hidden Chaos Mode** – A secret mode that unleashes multiple pranks in rapid sequence.

---

## 📂 Project Structure
```yaml
prank_toolbox/
│
├── assets/ # Images, sound effects, icons
│ └── boom.wav
│
├── self_destruct_deluxe.py # Main self destruct prank
├── infinite_update.py # Infinite update prank
├── useless_button.py # Useless button prank
├── fake_bsod.py # Fake blue screen prank
├── dancing_icons.py # Dancing icons prank
├── dashboard.py # Main launcher dashboard
├── PrankToolbox.exe # Compiled dashboard app (Windows)
└── README.md # This file
```

---

## 🚀 Installation & Usage

### **Option 1 — Run from Source**
You’ll need:
- Python 3.10+ installed
- `pip install playsound`

```bash
git clone https://github.com/<Pranav-MSK>/prank-toolbox.git
cd prank_toolbox
python dashboard.py
```

### **Option 2 — Run as an App (Windows)**
- Download the latest PrankToolbox_Installer.exe from the Releases page.
- Run the installer — it will add shortcuts to your desktop and Start Menu.
- Launch Prank Toolbox from the shortcut.
- Pick a prank… or find the secret Chaos Mode 😏.

### **🎮 How to Use**
Dashboard: Click any prank button to launch it in full screen.

Escape: Press Esc in most pranks to exit fullscreen mode.

Secret Chaos Mode: Click the ❌ exit button once to trigger 30 seconds of prank mayhem before you can close the app.

## 🛠 Built With
- Python

- Tkinter — GUI toolkit

- PyInstaller — Packaging into .exe

- Inno Setup — Windows installer creation

## 📸 Screenshots
(Add screenshots here after running the pranks)

## 🧩 Customization
Replace sounds in assets/ to give your pranks a unique vibe.

Modify funny_messages and error_messages lists in self_destruct_deluxe.py for personalized text.

Add your own .py prank scripts and register them in dashboard.py.

## ⚖️ License
This project is licensed under the MIT License — see the LICENSE file for details.

## 📝 Author
Pranav M S Krishnan
GitHub: @<Pranav-MSK>