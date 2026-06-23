from playwright.sync_api import sync_playwright

from src.database.connection import get_connection

from datetime import datetime

import re

from src.etl.raw_data_loader import insert_raw_scrape_data

def fetch_product_listings():
    """
        Fetches Amazon product listings from the database.
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT 
            pl.listing_id,
            pl.product_id,
            pl.retailer_product_name,
            pl.product_url
        FROM 
            product_listings pl
        JOIN stores s
            ON pl.store_id = s.store_id
        WHERE
            s.store_name = 'Amazon';
    """

    cursor.execute(query)
    listings = cursor.fetchall()

    cursor.close()
    connection.close()

    return listings

def scrape_product(listing):
    """
        Opens an Amazon product page and prints its title.
    """

    url = listing["product_url"]

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless= False
        )
        
        page = browser.new_page()
        
        page.goto(url)

        page.wait_for_selector("span#productTitle", timeout=10000)

        product_name = (
             page
             .locator("span#productTitle")
             .inner_text()
             .replace("\u200b", "")
             .strip()
        )

        price_text = (
             page
             .locator("span.a-price-whole")
             .first
             .inner_text()
             
        )

        current_price = int(re.sub(r"\D", "", price_text))


        browser.close()
        
        return {
             "listing_id": listing["listing_id"],
             "product_name": product_name,
             "current_price": current_price,
             "currency": "INR",
             "scraped_at": datetime.now(),
             "scraper_status": "Success"
             }
        
        

def main():
    listings = fetch_product_listings()
    # print(listings)

    result = scrape_product(listings[33])

    print(result)

    insert_raw_scrape_data(result)
    
if __name__ == "__main__":
        main()


