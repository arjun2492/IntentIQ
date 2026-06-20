from src.database.connection import get_connection

STORE_MAPPING = {
    "Sony": ["Amazon", "Flipkart", "Croma", "Reliance Digital", "Vijay Sales"],   # Sony
    "Apple": ["Amazon", "Flipkart", "Apple Store"],                                # Apple
    "Samsung": ["Amazon", "Flipkart", "Croma", "Reliance Digital"],                  # Samsung
    "OnePlus": ["Amazon", "Flipkart"],                                               # OnePlus
    "Bose": ["Amazon", "Flipkart"],                                               # Bose
    "JBL": ["Amazon", "Flipkart"],                                               # JBL
    "Sennheiser": ["Amazon", "Flipkart"],                                               # Sennheiser
    "Google": ["Amazon", "Flipkart"],                                               # Google
    "Dell": ["Amazon", "Reliance Digital"],                                       # Dell
    "HP": ["Amazon", "Reliance Digital"],                                      # HP
    "Lenovo": ["Amazon", "Reliance Digital"],                                      # Lenovo
    "Asus": ["Amazon", "Reliance Digital"]                                       # Asus
}



def fetch_products():
    """
    Fetches all products from the database    
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT 
            p. product_id,
            b. brand_name,
            p. product_name
        FROM 
            products p
        JOIN brands b
        ON p.brand_id = b.brand_id;
    """
    cursor.execute(query)
    products = cursor.fetchall()

    cursor.close()
    connection.close()    

    return products



def fetch_stores():
    """
    Fetches all stores from the database    
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT 
            store_id,
            store_name
        FROM 
            stores;
    """
    cursor.execute(query)
    stores = cursor.fetchall()

    cursor.close()
    connection.close()

    return stores


def generate_product_url(store_name, product_name):

     """
        Generates a realistic product URL based on the store and product name.
     """
     slug = (
         product_name
         .lower()
         .replace(" ", "-")
         .replace("(", "")
         .replace(")", "")
     )

     domains = {
         "Amazon": "amazon.in",
         "Flipkart": "flipkart.com",
         "Croma": "croma.com",
         "Reliance Digital": "reliancedigital.in",
         "Vijay Sales": "vijaysales.com",
         "Apple Store": "apple.com/in/store"
     }

     return f"https://{domains[store_name]}/{slug}"



def generate_product_listings(products, stores):
    """
    Generates retailer product listings.
    """

    listings = []

    # Creating lookup dictionary
    store_lookup = {
        store["store_name"]:store["store_id"]
        for store in stores
    }

    for product in products:
        allowed_stores = STORE_MAPPING[product["brand_name"]]
        
        for store_name in allowed_stores:
            listing = {
                "product_id": product["product_id"],
                "store_id": store_lookup[store_name],
                "retailer_product_name": product["product_name"],
                "product_url": generate_product_url(store_name, product["product_name"]),
                "listing_status": "Active" 
            }
            
            listings.append(listing)

    return listings


def product_listings_exist():
    """ 
    Checks whether product listings already exist in the database. 
    """
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT COUNT(*)
        FROM product_listings;    
    """

    cursor.execute(query)

    count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return count > 0

def insert_product_listings(listings):
    """ 
    Inserts generated product listings into the database. 
    """
    
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO product_listings(
            product_id, 
            store_id, 
            retailer_product_name, 
            product_url, 
            listing_status
        )
        VALUES(%s, %s, %s, %s, %s)
    """
    values = [
        (
            listing["product_id"], 
            listing["store_id"], 
            listing["retailer_product_name"], 
            listing["product_url"], 
            listing["listing_status"]
        )
        for listing in listings
    ]

    cursor.executemany(query, values)

    connection.commit()
    
    print(f"Successfully inserter {len(values)} product listings.")

    cursor.close()
    connection.close()



def main():

    if product_listings_exist():
        print("Product listings already exist Skipping generation")
        return


    products = fetch_products()
    stores = fetch_stores()
    listings = generate_product_listings(products, stores)
    insert_product_listings(listings) 
    


if __name__ == "__main__":
    main()

