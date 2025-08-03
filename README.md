# 🎙️ D-Phonix - Voice-Based Honeypot

![D-Phonix Banner](https://i.imgur.com/zpTzKQ3.png)

> **Author**: [Dushan Amarasekara](https://www.linkedin.com/in/dushan-amarasekara-6468182ba/)  
> **GitHub**: [Dushxn99](https://github.com/Dushxn99)

---

## 👁️ Overview

**D-Phonix** is a real-time **voice-activated honeypot** that detects suspicious phrases (like "password", "hack", "admin") through microphone input and responds with alerts, traps, and fake files to trick intruders. Perfect for cyber deception learning.

---

## 💡 Features

- 🎧 Continuous voice listening
- 🧠 Suspicious keyword detection
- 💬 AI voice response via `pyttsx3`
- 📁 Fake folder + password file trap
- 🧪 Logging of all heard phrases & alerts
- 📧 Email alerts to inbox (Gmail SMTP)
- 🛠️ `.exe` version built with PyInstaller
- 🖥️ Optional: GUI version & popup alerts (coming soon)

---

## 🐍 Tech Stack

- Python 3.x
- `pyttsx3` (text-to-speech)
- `speech_recognition`
- `smtplib` for email alerts
- `PyInstaller` to convert `.exe`

---

## 🚨 Sample Output

```bash
🎙️ D-Phonix is listening... (Press Ctrl+C to stop)
[Heard]: hack admin file
[D-Phonix Responds]: Intrusion detected.
📧 Email alert sent!
📁 Trap Created: /Fake_Passwords/Passwords.txt
🚀 Run D-Phonix
🔧 From Python Script
bash
Copy
Edit
pip install -r requirements.txt
python dphonix.py
🪟 Run as EXE
Double click dphonix.exe to silently run on Windows.

📦 Future Improvements
GUI control panel (start/stop/visible logs)

Password-protected trap files

Hidden .exe icon & stealth mode

System tray alert popup

🙌 Author
Dushan B.Y. Amarasekara
💼 LinkedIn
🐙 GitHub

“The quietest honeypot speaks the loudest when needed.” — D-Phonix

