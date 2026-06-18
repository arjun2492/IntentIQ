/*
==========================================================
IntentIQ - Purchase Intent Intelligence Platform

File: 03_operational_tables.sql
Description: Creates all operational tables.

Author: Arjun S Nair
==========================================================
*/

USE intentiq;

-- ======================================================
-- Table: users
-- ======================================================

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    whatsapp_number VARCHAR(20),
    state VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)ENGINE = InnoDB;

-- ======================================================
-- Table: watchlists
-- ======================================================

CREATE TABLE IF NOT EXISTS watchlists (
    watchlist_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    current_target_price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_watchlists_user_id
        FOREIGN KEY (user_id)
        REFERENCES users(user_id),

    CONSTRAINT fk_watchlists_product_id
        FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    CONSTRAINT uq_watchlists_user_product
        UNIQUE(user_id, product_id)

) ENGINE = InnoDB;

-- ======================================================
-- Table: target_price_history
-- ======================================================

CREATE TABLE IF NOT EXISTS target_price_history (
    target_history_id INT AUTO_INCREMENT PRIMARY KEY,
    watchlist_id INT NOT NULL,
    target_price DECIMAL(10,2) NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_target_price_history_watchlist_id
        FOREIGN KEY (watchlist_id)
        REFERENCES watchlists(watchlist_id)

)ENGINE = InnoDB;

-- ======================================================
-- Table: watchlist_events
-- ======================================================

CREATE TABLE IF NOT EXISTS watchlist_events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    watchlist_id INT NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    event_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_watchlist_events_watchlist_id
        FOREIGN KEY (watchlist_id)
        REFERENCES watchlists(watchlist_id)

)ENGINE = InnoDB;