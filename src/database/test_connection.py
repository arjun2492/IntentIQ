from src.database.connection import get_connection

def main():
    try:
        connection = get_connection()
        if connection.is_connected():
            print("Connected to IntentIQ database successfully")
        connection.close()
    except Exception as e:
        print(f"Connection failed: {e}")


if __name__ == "__main__":
    main()