import sqlite3

def create_users_table(db_path):
    """
    Creates a 'users' table with id, name, and email fields.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)

        conn.commit()
        print("✅ Table 'users' created (if it didn't already exist).")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Run the script
if __name__ == "__main__":
    create_users_table("sampleDB.db")

import sqlite3

def insert_data(db_path, table_name, data_dict):
    """
    Inserts a row into the specified table.

    :param db_path: Path to the database file
    :param table_name: Name of the table to insert into
    :param data_dict: Dictionary of column names and their values
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        columns = ', '.join(data_dict.keys())
        placeholders = ', '.join(['?' for _ in data_dict])
        values = tuple(data_dict.values())

        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, values)
        conn.commit()

        print(f"✅ Inserted data into '{table_name}': {data_dict}")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    db_file = "sampleDB.db"
    table = "users"
    new_row = {
        "name": "Alice Johnson",
        "email": "alice@example.com"
    }

    insert_data(db_file, table, new_row)
