/*
==========================================================
IntentIQ - Purchase Intent Intelligence Platform

File: 05_core_tables.sql
Description: Creates core business data tables.

Author: Arjun S Nair
==========================================================
*/

USE intentiq;

-- ======================================================
-- Table: price_history
-- ======================================================

CREATE TABLE IF NOT EXISTS price_history (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    store_id INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    scraped_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_price_history_product_id
        FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    CONSTRAINT fk_price_history_store_id
        FOREIGN KEY (store_id)
        REFERENCES stores(store_id),

    CONSTRAINT uq_price_history_record
        UNIQUE(product_id, store_id, scraped_at)

)ENGINE = InnoDB;

-- ======================================================
-- Table: notifications
-- ======================================================

CREATE TABLE IF NOT EXISTS notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    watchlist_id INT NOT NULL,
    price_id INT NOT NULL,
    notification_type VARCHAR(20) NOT NULL,
    notification_status VARCHAR(20) NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_notifications_watchlist_id
        FOREIGN KEY (watchlist_id)
        REFERENCES watchlists(watchlist_id),

    CONSTRAINT fk_notifications_price_id
        FOREIGN KEY (price_id)
        REFERENCES price_history(price_id)

) ENGINE = InnoDB;