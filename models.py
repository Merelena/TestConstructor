import sqlite3


def check_database():
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute("""""")
    print('Done')
    conn.close()