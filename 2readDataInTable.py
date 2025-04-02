import sqlite3

def list_tables(conn):
    """
    Returns a list of all user-defined table names in the database.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    return [table[0] for table in cursor.fetchall()]

def read_tables(db_path):
    """
    Connects to the database and reads all data from each table.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        tables = list_tables(conn)

        if not tables:
            print("No user-defined tables found.")
            return

        for table in tables:
            print(f"\n📋 Reading table: {table}")
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()

            # Fetch column names
            col_names = [description[0] for description in cursor.description]
            print(f"Columns: {col_names}")

            if rows:
                for row in rows:
                    print(row)
            else:
                print("No data in this table.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Run this script directly
if __name__ == "__main__":
    db_file = "sampleDB.db"  # Make sure this matches your database filename
    read_tables(db_file)
