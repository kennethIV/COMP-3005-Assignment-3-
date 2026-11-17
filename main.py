"""Command-line CRUD application for the COMP 3005 students database."""

import os
from datetime import date

import psycopg2
from psycopg2 import IntegrityError, Error


def connect_db():
    """Connect to PostgreSQL using local environment settings."""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "comp3005"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
    )


def getAllStudents():
    """Retrieve and display every student in the table."""
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM students ORDER BY student_id;")
                students = cur.fetchall()
        if not students:
            print("No students found.")
        else:
            for student in students:
                print(student)
    except Error as exc:
        print(f"Database error: {exc}")


def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a new student, letting PostgreSQL generate the ID."""
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO students
                       (first_name, last_name, email, enrollment_date)
                       VALUES (%s, %s, %s, %s) RETURNING student_id;""",
                    (first_name, last_name, email, enrollment_date),
                )
                student_id = cur.fetchone()[0]
        print(f"Student added successfully (ID: {student_id}).")
    except IntegrityError:
        print("Could not add student: the email must be unique and required fields cannot be empty.")
    except Error as exc:
        print(f"Database error: {exc}")


def updateStudentEmail(student_id, new_email):
    """Update one student's email address using the student ID."""
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE students SET email = %s WHERE student_id = %s;",
                    (new_email, student_id),
                )
                changed = cur.rowcount
        print("Email updated successfully." if changed else "Student ID not found.")
    except IntegrityError:
        print("Could not update email: it must be unique and non-null.")
    except Error as exc:
        print(f"Database error: {exc}")


def deleteStudent(student_id):
    """Delete the student whose ID matches the input."""
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
                deleted = cur.rowcount
        print("Student deleted successfully." if deleted else "Student ID not found.")
    except Error as exc:
        print(f"Database error: {exc}")


def main():
    """Show a menu so each required function can be demonstrated."""
    while True:
        print("\n--- Student Database Menu ---")
        print("1. View all students")
        print("2. Add student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            getAllStudents()
        elif choice == "2":
            first_name = input("First name: ").strip()
            last_name = input("Last name: ").strip()
            email = input("Email: ").strip()
            raw_date = input("Enrollment date (YYYY-MM-DD, optional): ").strip()
            if not first_name or not last_name or not email:
                print("First name, last name and email are required.")
                continue
            try:
                enrollment_date = date.fromisoformat(raw_date) if raw_date else None
            except ValueError:
                print("Invalid date. Please enter YYYY-MM-DD.")
                continue
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == "3":
            try:
                student_id = int(input("Student ID: "))
            except ValueError:
                print("Student ID must be an integer.")
                continue
            new_email = input("New email: ").strip()
            if not new_email:
                print("Email cannot be empty.")
                continue
            updateStudentEmail(student_id, new_email)
        elif choice == "4":
            try:
                student_id = int(input("Student ID to delete: "))
            except ValueError:
                print("Student ID must be an integer.")
                continue
            deleteStudent(student_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Select 1 through 5.")


if __name__ == "__main__":
    main()
