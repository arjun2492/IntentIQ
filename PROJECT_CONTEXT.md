# IntentIQ - Project Context Document (Version 1.0)

## Project Vision

IntentIQ is a **Purchase Intent Intelligence Platform** that enables consumers to set target prices for products they wish to buy while helping brands uncover purchase intent that typically remains invisible until a sale occurs.

By combining user watchlists, historical pricing, and purchase intent signals, IntentIQ generates actionable insights that help brands identify high-demand products, understand price sensitivity, and make informed decisions around promotions, clearance sales, inventory planning, and pricing strategy.

The project is primarily a **Data Engineering + Analytics portfolio project**, with a lightweight application layer to demonstrate real-world usage.

---

# Primary Objectives

## Consumer

* Create watchlists
* Set target prices
* Track prices across retailers
* Receive notifications when the target price is reached
* View price history

## Brand

* Measure purchase intent
* Identify demand before purchases occur
* Understand price sensitivity
* Analyze demand trends
* Support pricing and promotional decisions

---

# Technology Stack

Language

* Python

Database

* MySQL

Libraries

* pandas
* mysql-connector-python
* python-dotenv

Version Control

* Git / GitHub

Planned

* Playwright
* Power BI

---

# Final Project Structure

IntentIQ/

database/

* schema/
* seed/
* views/
* queries/

src/

* database/

  * connection.py

* data_generation/

  * generate_product_listings.py

* scraper/

* etl/

* notifications/

* analytics/

dashboard/

docs/

tests/

README.md

requirements.txt

.gitignore

.env

---

# Database Architecture

Reference Layer

* brands
* categories
* stores
* products

Operational Layer

* users
* watchlists
* target_price_history
* watchlist_events

Raw Layer

* raw_scrape_data

Core Business Layer

* product_listings
* price_history
* notifications

Analytics Layer

SQL Views

* vw_product_demand
* vw_price_segmentation
* vw_price_gap
* vw_monthly_growth
* vw_state_demand
* vw_category_performance
* vw_demand_velocity

---

# Analytics Scope

## Consumer Analytics

* Current Lowest Price
* Lowest Price Since Added
* Average Historical Price
* Price Trend

## Brand Analytics

* Demand Analytics
* Total Wishlists
* Most Tracked Products
* Price Segmentation
* Average Target Price
* Demand Velocity
* Category Performance
* Monthly Growth

---

# Data Sources

Seed Data

* Brands
* Categories
* Stores
* Products

Generated Data

* Product Listings

Future Generated Data

* Demo Users
* Demo Watchlists
* Demo Price History

Production Data

* Users
* Watchlists
* Target Price Changes
* Notifications

---

# Completed Milestones

Database Design

Completed

Database Dictionary

Completed

ER Diagram

Completed

Reference Tables

Completed

Operational Tables

Completed

Raw Layer

Completed

Core Business Layer

Completed

Seed Data

Completed

README

Completed

Python Foundation

Completed

Reusable Database Connection

Completed

Product Listings ETL Pipeline

Completed

---

# Product Listings Pipeline

Built using a simple ETL approach.

Extract

* fetch_products()
* fetch_stores()

Transform

* generate_product_url()
* generate_product_listings()

Load

* insert_product_listings()

Validation

* product_listings_exist()

The script is idempotent and safely skips generation if listings already exist.

---

# Important Design Decisions

1.

All Python code lives inside

src/

2.

SQL files remain inside

database/

3.

Run Python modules using

python -m src.module_name

instead of changing directories.

4.

Project architecture is frozen.

Avoid introducing unnecessary folders or abstractions.

5.

Only add complexity when a feature requires it.

6.

Every function should have one responsibility.

7.

One Git commit per completed feature.

---

# Current Seed Data

Brands

12

Categories

6

Stores

6

Products

36

Generated Product Listings

104

---

# Current Status

Completed

Database

Completed

Data Generation

Completed

Beginning Scraper Phase

---

# Next Milestone

Build a reusable Playwright scraping pipeline.

Planned structure:

src/

scraper/

amazon_scraper.py

flipkart_scraper.py

run_scraper.py

The scraper will initially only:

* Open a product URL
* Extract product name
* Extract current price
* Extract availability
* Return a Python dictionary

No database interaction initially.

After validation:

Scraper

↓

Raw Data Layer

↓

ETL

↓

Price History

↓

Notifications

↓

Analytics

---

# Development Philosophy

IntentIQ is intentionally being developed like a real software product rather than a tutorial project.

Key principles:

* Build incrementally
* Test every feature
* Keep functions small
* Avoid premature optimization
* Prefer readability over cleverness
* Use realistic datasets
* Focus on demonstrating Data Engineering skills

The emphasis is on engineering quality rather than simply producing a working application.

---

# Git Milestones

Completed

Initial project structure

Reference tables

Operational tables

Python database connection

Product listings generation pipeline

Next

Playwright scraper foundation
