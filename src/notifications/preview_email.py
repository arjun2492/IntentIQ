"""
==========================================================
DemandTrigger

File: preview_email.py

Description:
Sends a sample price drop email to preview the email template
without running the complete pipeline.

Author: Arjun S Nair
==========================================================
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from src.notifications.email_templates import (
    generate_price_drop_subject,
    generate_price_drop_text,
    generate_price_drop_html,
)

from src.notifications.email_sender import send_email

# ==========================
# Load Environment Variables
# ==========================

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

# ==========================
# Sample Notification
# ==========================

sample_notification = {
    "email": EMAIL_ADDRESS,
    "product_name": "Apple AirPods Pro (2nd Gen)",
    "store_name": "Amazon",
    "price": 18999,
    "current_target_price": 19000,
    "product_url": "https://www.amazon.in/"
}

# ==========================
# Generate Email
# ==========================

subject = generate_price_drop_subject(sample_notification)

text_body = generate_price_drop_text(sample_notification)

html_body = generate_price_drop_html(sample_notification)

# ==========================
# Send Email
# ==========================

if __name__ == "__main__":

    success = send_email(
        sample_notification,
        subject,
        text_body,
        html_body
    )

    if success:
        print("\nPreview email sent successfully!")
    else:
        print("\nFailed to send preview email.")