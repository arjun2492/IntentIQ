/*
==========================================================
IntentIQ - Purchase Intent Intelligence Platform

File: 04_raw_tables.sql
Description: Creates raw data layer tables.

Author: Arjun S Nair
==========================================================
*/

USE intentiq;

-- ======================================================
-- Table: raw_scrape_data
-- ======================================================

CREATE TABLE IF NOT EXISTS raw_scrape_data (
    scrape_id INT AUTO_INCREMENT PRIMARY KEY,
    listing_id INT NOT NULL,
    scraped_product_name VARCHAR(255) NOT NULL,
    scraped_price DECIMAL(10,2),
    availability VARCHAR(50),
    scrape_status VARCHAR(20) NOT NULL,
    scraped_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_raw_scrape_data_listing_id
        FOREIGN KEY (listing_id)
        REFERENCES product_listings(listing_id) 

) ENGINE = InnoDB;