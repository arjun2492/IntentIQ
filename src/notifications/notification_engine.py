from src.database.connection import get_connection
from src.config.logger import logger

# ==========================
# Fetch Functions
# ==========================

def fetch_price_alerts():
    """
    Fetches all watchlists where the latest price
    is less than or equal to the user's target price.
    """

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            w.watchlist_id,
            lp.price_id,
            lp.product_id,
            lp.store_id,
            lp.price,
            w.current_target_price
        FROM
            watchlists w
        JOIN latest_prices lp
            ON w.product_id = lp.product_id
        WHERE
            w.is_active = TRUE
            AND lp.price <= w.current_target_price;  
      
    """

    cursor.execute(query)

    alerts = cursor.fetchall()

    cursor.close()
    connection.close()

    logger.info(
        f"Found {len(alerts)} eligible price alert(s)."
        )

    return alerts

# ==========================
# Insert Functions
# ==========================

def insert_notifications(alerts):
    """
    Inserts eligible price alerts into the notifications table.
    """
    if not alerts:
        print("No notifications to create.")
        logger.info("No notifications to create.")
        return
    
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT IGNORE INTO notifications (
            watchlist_id,
            price_id,
            notification_type,
            notification_status,
            sent_at
        )
        VALUES (
            %s,
            %s,
            %s,
            %s,
            %s
        );
    """

    values = []

    for alert in alerts:

        values.append(
            (
            alert["watchlist_id"],
            alert["price_id"],
            "Price Drop",
            "Pending",
            None
            )
        )
    
    cursor.executemany(query, values)
    connection.commit()

    print(f"Inserted {cursor.rowcount} notification(s).")

    logger.info(
        f"Inserted {cursor.rowcount} notification(s)."
        )

    cursor.close()
    connection.close() 

# ==========================
# Main Pipeline
# ==========================

def main():
    
    try:
        alerts = fetch_price_alerts()
        
        insert_notifications(alerts)

    except Exception:
        logger.exception(
            "Notification engine failed."
        )
        raise

if __name__ == "__main__":
    main()