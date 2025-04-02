import sqlite3

def list_tables(db_path):
    """
    Connects to the SQLite database and lists all table names.
    
    :param db_path: Path to the .db SQLite database file
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to get all user-defined table names (ignoring system tables)
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()

        if tables:
            print(f"Tables in '{db_path}':")
            for table in tables:
                print(f" - {table[0]}")
        else:
            print(f"No user-defined tables found in '{db_path}'.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Run this script directly
if __name__ == "__main__":
    db_file = "sampleDB.db"  # Make sure this matches your file name
    list_tables(db_file)
