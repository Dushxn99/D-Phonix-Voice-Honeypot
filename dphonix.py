import pyttsx3
import speech_recognition as sr
from datetime import datetime
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# === SETUP: Voice Engine + Recognizer ===
engine = pyttsx3.init()
r = sr.Recognizer()

# === FOLDER SETUP: Logs ===
log_folder = "honeypot_logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
    if os.name == 'nt':  # Windows: hide folder
        os.system(f'attrib +h {log_folder}')

voice_log_file = os.path.join(log_folder, "voice_log.txt")
alert_log_file = os.path.join(log_folder, "alert_log.txt")
email_error_log = os.path.join(log_folder, "email_error_log.txt")

# === EMAIL SETUP ===
sender_email = "dphonix.alerts@gmail.com"
sender_password = "iasg zngg lcbg olnr"
receiver_email = "dphonix.alerts@gmail.com"  # Can replace with any inbox you want

def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("📧 Email alert sent!")
    except Exception as e:
        timestamp = datetime.now()
        with open(email_error_log, "a") as f:
            f.write(f"{timestamp} - Email send failed: {str(e)}\n")
        print("❌ Failed to send email alert. Error logged.")

# === SUSPICIOUS KEYWORDS + RESPONSES ===
suspicious_keywords = {
    "password": "Accessing password vault...",
    "admin": "Administrator privileges activated.",
    "delete": "Warning: Deletion protocol engaged.",
    "hack": "Intrusion detected.",
    "login": "Logging into root system...",
    "shutdown": "System shutting down...",
    "virus": "Malware execution initiated.",
    "secret": "Confidential file opened.",
    "attack": "Launching attack vector...",
    "credit card": "Credit card vault accessed.",
    "bank": "Connecting to bank servers...",
    "files": "Opening confidential files.",
    "open folder": "Exploring system directories..."
}

# === SPEAKING FUNCTION ===
def respond(message):
    print(f"[D-Phonix Responds]: {message}")
    engine.say(message)
    engine.runAndWait()

# === TRAP FOLDER ===
def create_fake_folder():
    folder_name = "Fake_Passwords"
    file_name = "Passwords.txt"
    folder_path = os.path.join(os.getcwd(), folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"[Trap Created] Folder: {folder_path}")

    fake_file = os.path.join(folder_path, file_name)
    with open(fake_file, "w") as f:
        f.write("Facebook: admin@example.com | Password: 123456\n")
        f.write("Bank: user@bank.com | Password: qwerty\n")
        f.write("Email: hacker@evil.com | Password: letmein123\n")

    print(f"[Trap Created] File: {fake_file}")

# === INTRO MESSAGE ===
respond("Hello! This is D-Phonix, your voice-based honeypot. I am now listening continuously.")

# === LISTENING LOOP ===
while True:
    with sr.Microphone() as source:
        print("\n🎙️ D-Phonix is listening... (Press Ctrl+C to stop)")

        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            timestamp = datetime.now()
            print(f"[Heard]: {text}")

            # === LOG VOICE ===
            with open(voice_log_file, "a") as log:
                log.write(f"{timestamp} - {text}\n")

            # === CHECK KEYWORDS ===
            suspicious_found = False
            for keyword in suspicious_keywords:
                if keyword in text.lower():
                    suspicious_found = True
                    alert_msg = f"{timestamp} - ALERT: Suspicious keyword '{keyword}' in: '{text}'"

                    # === LOG ALERT ===
                    with open(alert_log_file, "a") as alert:
                        alert.write(alert_msg + "\n")

                    print(alert_msg)
                    respond("Warning. Suspicious keyword detected.")
                    respond(suspicious_keywords[keyword])

                    # === SEND EMAIL ALERT ===
                    send_email("🚨 D-Phonix Alert", alert_msg)

                    # === TRAP ===
                    create_fake_folder()
                    break

            if not suspicious_found:
                respond("Command received and logged.")

        except sr.WaitTimeoutError:
            print("⏱️ No voice detected.")
        except sr.UnknownValueError:
            print("🤖 D-Phonix didn't understand that.")
            respond("Sorry, I did not understand that.")
        except sr.RequestError:
            print("❌ Could not reach the voice recognition service.")
            respond("Voice service is currently unavailable.")
        except KeyboardInterrupt:
            print("\n🛑 Stopping D-Phonix honeypot.")
            respond("Shutting down honeypot. Stay safe.")
            break

        time.sleep(2)
