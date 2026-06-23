# INTENTIQ - DEVELOPMENT HANDOFF DOCUMENT

## Project Overview

IntentIQ is a Purchase Intent Intelligence Platform.

Consumer Side:

* Users create watchlists.
* Users set target prices.
* Users receive notifications when prices drop below their target price.
* Users can view price history.

Brand Side:

* Brands can analyze purchase intent before a purchase occurs.
* Brands can understand demand trends.
* Brands can identify price sensitivity.
* Brands can use insights for promotions, pricing strategy, inventory planning, and clearance sales.

Primary focus of the project:

* Data Engineering
* ETL Pipelines
* SQL
* Python
* Web Scraping
* Analytics
* Power BI

Frontend/UI is intentionally lightweight.

---

## CURRENT PROJECT STATUS

Approximate completion: 45%

Completed:

* Project definition
* Architecture
* Data dictionary
* ERD
* DBML
* Database implementation
* Seed data
* Python foundation
* Product listings ETL pipeline

Currently Working On:

* Amazon scraper using Playwright

Next Phases:

* Complete scraper
* Raw data ingestion
* ETL pipeline
* Price history updates
* Notifications
* Analytics views
* Power BI dashboard

---

## PROJECT STRUCTURE

IntentIQ/

database/
├── schema/
├── seed/
├── views/
└── queries/

src/
├── database/
│   └── connection.py
│
├── data_generation/
│   └── generate_product_listings.py
│
├── scraper/
│   └── amazon_scraper.py
│
├── etl/
├── notifications/
└── analytics/

dashboard/
docs/
tests/

README.md
requirements.txt
.env

---

## DATABASE LAYERS

Reference Layer

* brands
* categories
* stores
* products
* product_listings

Operational Layer

* users
* watchlists
* target_price_history
* watchlist_events

Raw Layer

* raw_scrape_data

Core Business Layer

* price_history
* notifications

Analytics Layer

Planned SQL Views:

* vw_product_demand
* vw_price_segmentation
* vw_price_gap
* vw_monthly_growth
* vw_state_demand
* vw_category_performance
* vw_demand_velocity

---

## IMPORTANT DATABASE DECISIONS

notifications was moved from Operational Layer to Core Business Layer.

price_history has:

UNIQUE(product_id, store_id, scraped_at)

product_listings is generated data.

Current generated listings:
104 rows

Real retailer URLs exist only for a subset of products.

All other listings use generated placeholder URLs.

---

## PYTHON DATABASE CONNECTION

Location:

src/database/connection.py

Function:

get_connection()

Used throughout the project.

Imports:

from src.database.connection import get_connection

Scripts are executed from project root using:

python -m module.path

Example:

python -m src.scraper.amazon_scraper

---

## PRODUCT LISTINGS PIPELINE

Location:

src/data_generation/generate_product_listings.py

Functions:

fetch_products()

fetch_stores()

generate_product_url()

generate_product_listings()

product_listings_exist()

insert_product_listings()

Main ETL Flow:

Products
+
Stores
↓
Generate Listings
↓
Insert into product_listings

Script is idempotent.

If listings already exist:

"Product listings already exist. Skipping generation."

---

## IMPORTANT IMPLEMENTATION CHANGE

fetch_products() was modified.

Instead of returning:

brand_id

it now joins brands table and returns:

brand_name

STORE_MAPPING uses brand names, NOT brand IDs.

Example:

STORE_MAPPING = {
"Sony": [...],
"Apple": [...],
...
}

---

## REAL PRODUCT URL SUPPORT

generate_product_url() checks:

PRODUCT_URL_MAPPING

before generating a placeholder URL.

Example:

PRODUCT_URL_MAPPING = {
("Sony WH-1000XM5", "Amazon"):
"https://www.amazon.in/Sony-WH-1000XM5-Wireless-Cancelling-Headphones/dp/B09XS7JWHH?th=1",

```
("Sony WH-1000XM5", "Flipkart"):
    "https://www.flipkart.com/sony-wh1000xm5-silver-bluetooth-wired/p/itm96f759ebab85d",
```

}

If mapping exists:
Use real URL.

Otherwise:
Generate placeholder URL.

---

## CURRENT SCRAPER STATUS

File:

src/scraper/amazon_scraper.py

Playwright installed.

Chromium installed.

Browser successfully launches.

Amazon product page successfully loads.

Database successfully feeds URLs into scraper.

Current flow:

fetch_product_listings()
↓
scrape_product()
↓
Return dictionary

---

## CURRENT SCRAPER FUNCTIONS

fetch_product_listings()

Purpose:

Fetch Amazon listings from database.

Current query:

SELECT
pl.listing_id,
pl.product_id,
pl.retailer_product_name,
pl.product_url
FROM product_listings pl
JOIN stores s
ON pl.store_id = s.store_id
WHERE s.store_name = 'Amazon';

Returns:

[
{
"listing_id": 1,
"product_id": 1,
"retailer_product_name": "...",
"product_url": "..."
}
]

---

## CURRENT SCRAPER IMPLEMENTATION

Current scrape_product():

* Opens browser
* Opens URL
* Waits for selector
* Extracts product title

Working selector:

span#productTitle

Current extraction:

product_name = (
page
.locator("span#productTitle")
.inner_text()
.replace("\u200b", "")
.strip()
)

Current return:

{
"product_name": product_name
}

---

## IMPORTANT SCRAPER DECISION

Availability is NOT currently part of the data model.

Do NOT focus on availability.

Priority is:

1. Product Name
2. Current Price
3. Store raw scrape data
4. ETL
5. Price History
6. Notifications

availability is considered optional for MVP.

---

## CURRENT DEVELOPMENT MILESTONE

Product name extraction works successfully.

Next task:

Extract current price from Amazon page.

Goal:

Return:

{
"listing_id": listing["listing_id"],
"product_name": product_name,
"current_price": 22990
}

Convert:

₹22,990

into:

22990

(integer)

This will be the next step in scraper development.

---

## DEVELOPMENT PHILOSOPHY

* Keep functions small.
* One responsibility per function.
* Avoid premature abstraction.
* Only create shared modules when 2+ scripts need them.
* Use realistic data.
* Build incrementally.
* Test after every milestone.
* One Git commit per completed feature.

The project is intentionally being developed like a real data engineering system rather than a tutorial project.
