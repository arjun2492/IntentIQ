/*
==========================================================
IntentIQ

File: 03_stores.sql

Description:
Populates the stores reference table.

Author: Arjun S Nair
==========================================================
*/

USE intentiq;

INSERT INTO stores(store_name, store_type, website)
VALUES
    ('Amazon', 'Marketplace', 'https://www.amazon.in'),
    ('Flipkart', 'Marketplace', 'https://www.flipkart.com'),
    ('Croma', 'Retail', 'https://www.croma.com'),
    ('Reliance Digital', 'Retail', 'https://www.reliancedigital.in'),
    ('Vijay Sales', 'Retail', 'https://www.vijaysales.com'),
    ('Apple Store', 'Brand Store', 'https://www.apple.com/in/store');