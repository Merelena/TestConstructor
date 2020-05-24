import sqlite3


global cursor, conn


def open_db():
    global cursor, conn
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()


def check_database(subject):
    global cursor
    cursor.execute("""
    SELECT subject_name FROM Subjects
    """)
    response = cursor.fetchall()
    return (subject,) in response


def add_subject_to_db(subject):
    global cursor, conn
    cursor.execute(f"""
    INSERT INTO Subjects(subject_name) VALUES ('{subject}');
    """)
    conn.commit()


def create_test(name):
    global cursor, conn
    cursor.execute(f"""
        INSERT INTO Tests(test_name) VALUES ('{name}');
        """)
    conn.commit()


def save_new_task(task, level, id_subject, test_name):
    global cursor, conn
    cursor.execute(f"""
            INSERT INTO Tasks(task_text, level, id_subject, id_test) 
VALUES ('{task}', '{level}', '{id_subject}', '{search_test_id(test_name)[0]}');
            """)
    conn.commit()


def save_task(task, level, id_task):
    global cursor, conn
    cursor.execute(f"""
                UPDATE Tasks  SET task_text='{task}', level='{level}' WHERE id_tasks='{id_task}';
                """)
    conn.commit()


def search_subject_id(subject):
    global cursor
    cursor.execute(f"""
            SELECT id_subject FROM Subjects WHERE subject_name='{subject}';
            """)
    print('Done')
    return cursor.fetchall()[0][0]


def search_test_id(test_name):
    global cursor
    cursor.execute(f"""
                SELECT DISTINCT id_test FROM Tests WHERE test_name='{test_name}';
                """)
    response = cursor.fetchall()[0]
    return response if response else None


def delete_test(test_name):
    global cursor, conn
    cursor.execute(f"""
                       DELETE FROM Tasks WHERE id_test='{search_test_id(test_name)}';
                       """)
    cursor.execute(f"""
                   DELETE FROM Tests WHERE test_name='{test_name}';
                   """)
    conn.commit()


def search_task(task, level, id_subject, test_name):
    global cursor
    id_test = search_test_id(test_name)[0]
    """conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()"""
    cursor.execute(f"""SELECT id_tasks FROM Tasks WHERE task_text='{task}' AND level='{level}' 
AND id_subject='{id_subject}' AND id_test='{id_test}';""")
    return cursor.fetchall()[0][0]


def show_tasks(test_name, id_subject):
    global cursor
    id_test = search_test_id(test_name)
    """conn = sqlite3.connect('TestConstructorDB.db')
     cursor = conn.cursor()"""
    cursor.execute(f"""SELECT id_tasks, level FROM Tasks WHERE id_test IN (
SELECT id_test FROM Tests WHERE test_name='{test_name}') AND id_subject='{id_subject}';""")
    response = cursor.fetchall()
    return response


def show_tests(subject):
    global cursor
    cursor.execute(
        f"""SELECT DISTINCT test_name FROM Tests WHERE id_test in (SELECT id_test FROM Tasks WHERE id_subject in 
(SELECT id_subject FROM Subjects WHERE subject_name='{subject}'));""")
    print('Done show tests')
    return cursor.fetchall()


def open_task(id_task):
    global cursor
    cursor.execute(
        f"""SELECT task_text, level FROM Tasks WHERE id_tasks='{id_task}';""")
    print('Done open task')
    return cursor.fetchall()


def delete_task(id_task):
    global cursor, conn
    cursor.execute(
        f"""DELETE FROM Tasks WHERE id_tasks='{id_task}';""")
    print('Done delete task')
    conn.commit()


def number_of_tests(subject):
    global cursor
    cursor.execute(
        f"""SELECT COUNT(id_test) FROM Tasks WHERE id_subject in (SELECT id_subject FROM Subjects WHERE subject_name='{subject}');""")
    return (cursor.fetchall())[0][0]


def get_tasks(level, id_test):
    global cursor
    cursor.execute(f""" SELECT task_text FROM Tasks WHERE level='{level}' AND id_test='{id_test}';""")
    tasks = cursor.fetchall()
    yield tasks