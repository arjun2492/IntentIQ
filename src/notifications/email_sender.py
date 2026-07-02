"""
==========================================================
IntentIQ

File: email_sender.py

Description:
Utility for sending email notifications to users.

Author: Arjun S Nair
==========================================================
"""

import os
import smtplib

from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv

# ==========================
# Load Environment Variables
# ==========================

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR/".env")

# ==========================
# Email Configuration
# ==========================

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

# ==========================
# Send Email
# ==========================

def send_email(notification, subject, text_body, html_body):
    """
    Sends a plain text email.

    Returns:
        True  -> Email sent successfully
        False -> Failed to send
    """
    
    try:
        message = EmailMessage()

        message["From"] = EMAIL_ADDRESS
        message["To"] = notification["email"]
        message["Subject"] = subject

        message.set_content(text_body)

        message.add_alternative(
            html_body,
            subtype="html"
            )

        with smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        ) as smtp:
            
            smtp.starttls()

            smtp.login(
                EMAIL_ADDRESS,
                EMAIL_PASSWORD
            )
            
            smtp.send_message(message)

        print("Email sent successfully")

        return True

    except Exception as e:

        print("Email sending failed")

        print(e)

        return False

# ==========================
# Test
# ==========================

if __name__ == "__main__":

    send_email(
        recipient_email= EMAIL_ADDRESS,
        subject="IntentIQ Test Email",
        body="""
Congratulations!

Your IntentIQ email notification system is working successfully.

- IntentIQ
"""

    )        
