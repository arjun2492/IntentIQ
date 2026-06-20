import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

# To load environment variables from .env
BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

def get_connection():
    
    """
    Creates and returns a connection to the IntentIQ MySQL database.
    """

    connection = mysql.connector.connect(
      host = os.getenv("DB_HOST"),
      port = int(os.getenv("DB_PORT")),
      database = os.getenv("DB_NAME"),
      user = os.getenv("DB_USER"),
      password = os.getenv("DB_PASSWORD")  
    )

    return connection