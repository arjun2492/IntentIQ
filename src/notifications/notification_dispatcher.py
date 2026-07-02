"""
==========================================================
IntentIQ

File: notification_dispatcher.py

Description:
Fetches pending notifications, simulates sending them,
and updates their status to 'Sent'.

Author: Arjun S Nair
==========================================================
"""

from src.database.connection import get_connection

from src.notifications.email_sender import send_email
from src.notifications.email_templates import (
    generate_price_drop_subject,
    generate_price_drop_text,
    generate_price_drop_html
    )

# ==========================
# Fetch Functions
# ==========================

def fetch_pending_notifications():
    """
    Fetches all pending notifications with the
    information required to send the notification.
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            n.notification_id,
            u.email,
            u.whatsapp_number,
            p.product_name,
            s.store_name,
            lp.price,
            w.current_target_price,
            pl.product_url,
            n.notification_type
        FROM
            notifications n
        JOIN watchlists w
            ON n.watchlist_id = w.watchlist_id
        
        JOIN users u
            ON w.user_id = u.user_id

        JOIN products p
            ON w.product_id = p.product_id

        JOIN latest_prices lp
            ON n.price_id = lp.price_id
        
        JOIN product_listings pl
            ON lp.product_id = pl.product_id
                AND lp.store_id = pl.store_id

        JOIN stores s
            ON lp.store_id = s.store_id

        WHERE 
            n.notification_status = 'Pending'; 
    """
    cursor.execute(query)

    notifications = cursor.fetchall()

    cursor.close()
    connection.close()

    return notifications

# ==========================
# Update Functions
# ==========================

def update_notification_status(notification_id, status):
    """
    Updates the notification delivery status.
    """
    connection =  get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE notifications
        SET 
            notification_status = %s,
            sent_at = NOW()
        WHERE
            notification_id = %s;
    """
    cursor.execute(query, (status, notification_id,))
    
    connection.commit()
    
    cursor.close()
    connection.close()

# ==========================
# Dispatcher
# ==========================

def dispatch_notifications():
    """
    Sends all pending email notifications.
    """
    notifications = fetch_pending_notifications()

    if not notifications:
        print("No pending notifications.")
        return
    
    for notification in notifications:

        try: 
            subject = generate_price_drop_subject(notification)
            text_body = generate_price_drop_text(notification)
            html_body = generate_price_drop_html(notification)
            
            notification_sent = send_email(
                notification,
                subject,
                text_body,
                html_body
                )
           

            if notification_sent:
                update_notification_status(
                    notification["notification_id"],
                    "Sent"
                )

                print(
                    f"Email sent for "
                    f"{notification['product_name']}"
                )

            else:
                update_notification_status(
                    notification["notification_id"],
                    "Failed"
                )

                print(
                    f"Email failed for "
                    f"{notification['product_name']}"
                )

        except Exception as e:

            update_notification_status(
                notification["notification_id"],
                "Failed"
            )

            print(
                f"Failed: "
                f"{notification['product_name']}"
            )

            print(e)




# ==========================
# Main
# ==========================

def main():

    dispatch_notifications()


if __name__ == "__main__":
    main()

