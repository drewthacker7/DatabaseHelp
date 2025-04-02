import sqlite3

def update_record(db_path, table_name, update_dict, condition_dict):
    """
    Updates a record in the given table.

    :param db_path: Path to the SQLite database file
    :param table_name: Table to update
    :param update_dict: Dictionary of columns and their new values
    :param condition_dict: Dictionary of conditions for WHERE clause
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Build SET part
        set_clause = ', '.join([f"{col}=?" for col in update_dict])
        set_values = list(update_dict.values())

        # Build WHERE part
        where_clause = ' AND '.join([f"{col}=?" for col in condition_dict])
        where_values = list(condition_dict.values())

        sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause};"
        cursor.execute(sql, set_values + where_values)
        conn.commit()

        print(f"✅ Updated {cursor.rowcount} record(s) in '{table_name}'.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    db_file = "sampleDB.db"
    table = "users"
    
    # Example: Change email for user with name "Alice Johnson"
    update_values = {
        "email": "alice.j@newdomain.com"
    }
    where_condition = {
        "name": "Alice Johnson"
    }

    update_record(db_file, table, update_values, where_condition)
