import sqlite3

def connect_db():
    return sqlite3.connect("vitb360.db")


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        name TEXT,
        branch TEXT,
        semester TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_student_db(student_id, name, branch, semester):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students (student_id, name, branch, semester)
    VALUES (?, ?, ?, ?)
    """, (student_id, name, branch, semester))

    conn.commit()
    conn.close()


def get_students_db():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()
    return students


def delete_student_db(student_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()
def update_student_db(student_id, name, branch, semester):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET name = ?, branch = ?, semester = ?
    WHERE student_id = ?
    """, (name, branch, semester, student_id))

    conn.commit()
    conn.close()
def create_academic_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS academic_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        subject_name TEXT,
        faculty TEXT,
        slot TEXT,
        credits TEXT,
        cat1 REAL,
        cat2 REAL,
        term_end REAL,
        internals REAL,
        attendance REAL
    )
    """)

    conn.commit()
    conn.close()
def add_academic_record(student_id, subject_name, faculty, slot, credits):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO academic_records
    (student_id, subject_name, faculty, slot, credits)
    VALUES (?, ?, ?, ?, ?)
    """, (student_id, subject_name, faculty, slot, credits))

    conn.commit()
    conn.close()
def update_cat1(student_id, subject_name, marks):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE academic_records
    SET cat1 = ?
    WHERE student_id = ? AND subject_name = ?
    """, (marks, student_id, subject_name))

    conn.commit()
    conn.close()


def update_cat2(student_id, subject_name, marks):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE academic_records
    SET cat2 = ?
    WHERE student_id = ? AND subject_name = ?
    """, (marks, student_id, subject_name))

    conn.commit()
    conn.close()


def update_term_end(student_id, subject_name, marks):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE academic_records
    SET term_end = ?
    WHERE student_id = ? AND subject_name = ?
    """, (marks, student_id, subject_name))

    conn.commit()
    conn.close()


def update_internals(student_id, subject_name, marks):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE academic_records
    SET internals = ?
    WHERE student_id = ? AND subject_name = ?
    """, (marks, student_id, subject_name))

    conn.commit()
    conn.close()


def update_attendance(student_id, subject_name, attendance):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE academic_records
    SET attendance = ?
    WHERE student_id = ? AND subject_name = ?
    """, (attendance, student_id, subject_name))

    conn.commit()
    conn.close()
    