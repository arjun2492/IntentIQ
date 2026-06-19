/*
==========================================================
IntentIQ - Purchase Intent Intelligence Platform

File: 04_products.sql

Description:
Populates the products reference table.

Author: Arjun S Nair
==========================================================
*/

USE intentiq;

INSERT INTO products
(brand_id, category_id, product_name, model_number)
VALUES

-- ======================================================
-- Headphones (Category ID = 1)
-- ======================================================

(1,1,'Sony WH-1000XM5','WH-1000XM5'),
(5,1,'Bose QuietComfort Ultra','QC Ultra'),
(6,1,'JBL Live 770NC','Live 770NC'),
(7,1,'Sennheiser Momentum 4','Momentum 4'),
(4,1,'OnePlus Nord Wired Headphones','Nord Wired'),
(1,1,'Sony WH-CH720N','WH-CH720N'),

-- ======================================================
-- Earbuds (Category ID = 2)
-- ======================================================

(1,2,'Sony WF-1000XM5','WF-1000XM5'),
(2,2,'Apple AirPods Pro (2nd Gen)','AirPods Pro 2'),
(4,2,'OnePlus Buds Pro 3','Buds Pro 3'),
(6,2,'JBL Live Beam 3','Live Beam 3'),
(7,2,'Sennheiser Momentum True Wireless 4','MTW4'),
(3,2,'Samsung Galaxy Buds3 Pro','Galaxy Buds3 Pro'),

-- ======================================================
-- Smartphones (Category ID = 3)
-- ======================================================

(2,3,'Apple iPhone 16','iPhone 16'),
(2,3,'Apple iPhone 16 Pro','iPhone 16 Pro'),
(3,3,'Samsung Galaxy S25','Galaxy S25'),
(3,3,'Samsung Galaxy S25 Ultra','Galaxy S25 Ultra'),
(4,3,'OnePlus 13','OnePlus 13'),
(8,3,'Google Pixel 9','Pixel 9'),
(8,3,'Google Pixel 9 Pro','Pixel 9 Pro'),
(3,3,'Samsung Galaxy A56','Galaxy A56'),

-- ======================================================
-- Smartwatches (Category ID = 4)
-- ======================================================

(2,4,'Apple Watch Series 10','Series 10'),
(3,4,'Samsung Galaxy Watch Ultra','Watch Ultra'),
(3,4,'Samsung Galaxy Watch 7','Watch 7'),
(4,4,'OnePlus Watch 2','Watch 2'),
(2,4,'Apple Watch SE','Watch SE'),
(8,4,'Google Pixel Watch 3','Watch 3'),

-- ======================================================
-- Laptops (Category ID = 5)
-- ======================================================

(2,5,'Apple MacBook Air M4','MacBook Air M4'),
(2,5,'Apple MacBook Pro M4','MacBook Pro M4'),
(9,5,'Dell XPS 13','XPS 13'),
(10,5,'HP Spectre x360','Spectre x360'),
(11,5,'Lenovo Yoga 9i','Yoga 9i'),
(12,5,'Asus Zenbook 14 OLED','Zenbook 14 OLED'),

-- ======================================================
-- Tablets (Category ID = 6)
-- ======================================================

(2,6,'Apple iPad Air','iPad Air'),
(2,6,'Apple iPad Pro','iPad Pro'),
(3,6,'Samsung Galaxy Tab S10+','Tab S10+'),
(8,6,'Google Pixel Tablet','Pixel Tablet');