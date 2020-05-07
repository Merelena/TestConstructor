import sqlite3


def check_database(subject):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT subject_name FROM Subjects
    """)
    response = cursor.fetchall()
    return (subject,) in response;
    print('Done')
    conn.commit()
    conn.close()


def add_subject_to_db(subject):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    INSERT INTO Subjects(subject_name) VALUES ('{subject}');
    """)
    print('Done')
    conn.commit()
    conn.close()