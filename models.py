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


def create_test(name):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO Tests(test_name) VALUES ('{name}');
        """)
    print('Done')
    conn.commit()
    conn.close()



def save_new_task(task, level, id_subject, test_name):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(f"""
            INSERT INTO Tasks(task_text, level, id_subject, id_test) 
VALUES ('{task}', '{level}', '{id_subject}', '{search_test_id(test_name)}');
            """)
    print('z')
    conn.commit()
    conn.close()


def save_task(task, level, id_task):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(f"""
                UPDATE Tasks  SET task_text='{task}', level='{level}' WHERE id_tasks='{id_task}';
                """)
    print('z')
    conn.commit()
    conn.close()


def search_subject_id(subject):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(f"""
            SELECT id_subject FROM Subjects WHERE subject_name='{subject}';
            """)
    print('Done')
    return cursor.fetchall()[0]
    conn.close()


def search_test_id(test_name):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(f"""
                SELECT id_test FROM Tests WHERE test_name='{test_name}';
                """)
    print('Done')
    return cursor.fetchall()[0]
    conn.close()


def delete_test(test_name):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(f"""
                   DELETE FROM Tests WHERE test_name='{test_name}';
                   """)
    cursor.execute(f"""
                       DELETE FROM Tasks WHERE id_test='{search_test_id(test_name)}';
                       """)
    print('Done')
    conn.commit()
    conn.close()


def search_task(task, level, id_subject, test_name):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    id_test = search_test_id(test_name)
    cursor.execute(f"""SELECT id_tasks FROM Tasks WHERE task_text='{task}' AND level='{level}' 
AND id_subject='{id_subject}' AND id_test='{id_test}';""")
    print('Done save task')
    return cursor.fetchall()[0][0]
    conn.close()


def show_tasks(test_name, id_subject):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    id_test = search_test_id(test_name)
    cursor.execute(f"""SELECT id_tasks, level FROM Tasks WHERE id_test='{search_test_id(test_name)}' AND id_subject='{id_subject}';""")
    print('Done show tasks')
    return cursor.fetchall()
    conn.close()

def show_tests():
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT DISTINCT test_name FROM Tests;""")
    print('Done show tests')
    return cursor.fetchall()
    conn.close()

def open_task(id_task):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT task_text, level FROM Tasks WHERE id_tasks='{id_task}';""")
    print('Done open task')
    return cursor.fetchall()
    conn.close()

def delete_task(id_task):
    conn = sqlite3.connect('TestConstructorDB.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""DELETE FROM Tasks WHERE id_tasks='{id_task}';""")
    print('Done delete task')
    return cursor.fetchall()
    conn.close()
