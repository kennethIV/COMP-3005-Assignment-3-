# COMP 3005 — PostgreSQL Student Database Application

A Python command-line application that connects to PostgreSQL and performs Create, Read, Update, and Delete (CRUD) operations on a `students` table.

A Python application that uses PostgreSQL to manage student records.

Requirements:

Python 3

PostgreSQL and pgAdmin

psycopg2-binary
//

Setup:

Create a database called comp3005 in pgAdmin.

Run database.sql in the Query Tool to create the table and add the sample students.

Install the required package:

pip install -r requirements.txt

In PowerShell, enter your PostgreSQL connection details:

$env:DB_NAME="comp3005"
$env:DB_USER="postgres"
$env:DB_PASSWORD="YOUR_PASSWORD"
python main.py

Replace YOUR_PASSWORD with your PostgreSQL password.
//

Functions:

getAllStudents() – Displays all students.

addStudent() – Adds a student.

updateStudentEmail() – Updates a student's email.

deleteStudent() – Deletes a student.

The program uses a menu to select each operation.
//
Demo Video - https://youtu.be/ww7lQFZ4pw4

Watch the demonstration

The video shows the database setup and all four functions working.
//
Files:

main.py – Python application

database.sql – Table creation and sample data

requirements.txt – Required Python package

README.md – Setup instructions