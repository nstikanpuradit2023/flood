import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# --- LOAD ENV VARIABLES ---
load_dotenv()  # Loads variables from .env file

sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
receiver_email = "pkashish852@gmail.com"  # Change this to recipient email

# --- EMAIL CONTENT ---
subject = "Test Email via Python and .env"
body = "Hello,\n\nmazak mein bheja hai.env file.\n\nRegards,\nPython Script"

# --- CREATE EMAIL MESSAGE ---
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# --- SEND EMAIL ---
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

except Exception as e:
    print("Failed to send email:", e)
