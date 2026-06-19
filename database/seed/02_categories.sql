/*
==========================================================
IntentIQ

File: 02_categories.sql

Description:
Populates the categories reference table.

Author: Arjun S Nair
==========================================================
*/

USE intentiq;

INSERT INTO categories(category_name)
VALUES 
    ('Headphones'),
    ('Earbuds'),
    ('Smartphones'),
    ('Smartwatches'),
    ('Laptops'),
    ('Tablets');