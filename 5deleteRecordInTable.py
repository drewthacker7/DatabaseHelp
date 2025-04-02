import sqlite3

def delete_record(db_path, table_name, condition_dict):
    """
    Deletes record(s) from the given table based on a condition.

    :param db_path: Path to the SQLite database file
    :param table_name: Table to delete from
    :param condition_dict: Dictionary of conditions for the WHERE clause
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Build WHERE clause
        where_clause = ' AND '.join([f"{col}=?" for col in condition_dict])
        where_values = list(condition_dict.values())

        sql = f"DELETE FROM {table_name} WHERE {where_clause};"
        cursor.execute(sql, where_values)
        conn.commit()

        print(f"🗑️ Deleted {cursor.rowcount} record(s) from '{table_name}'.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    db_file = "sampleDB.db"
    table = "users"

    # Example: Delete user with name "Alice Johnson"
    condition = {
        "name": "Alice Johnson"
    }

    delete_record(db_file, table, condition)
