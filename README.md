# VITB360: Student Academic and Performance Hub

## About the Project

VITB360 is a simple command-line based student academic and performance management system developed as a first-year Python project.

The idea behind the project was to create something more useful than just storing student marks, but make something slightly ec=xciting and motivating from the student point of view. The system allows different users to access different parts of the academic record, while also giving students a small dashboard to understand their performance.

The project uses Python for the main program and SQLite for storing student and academic records.

## What Can VITB360 Do?

The system has three main sections:

### 1. Administrator

The Administrator can:

* Add student records
* View student records
* Search for a student
* Update student details
* Delete student records
* Add subjects for students
* Prevent duplicate student IDs
* Prevent duplicate subjects for the same student

### 2. Faculty

The Faculty section can be used to:

* View student records
* Add CAT1 marks
* Add CAT2 marks
* Add Term End marks
* Add Internal marks
* Add attendance

### 3. Student

The Student section includes:

* Student Dashboard
* Subject-wise performance
* Academic average
* Average attendance
* Strongest subject
* Achievement Wall
* What-If Grade Simulator

## Marks and Grade Calculation

The weighted score is calculated using the following weightage, followed in our college VIT Bhopal University:

* CAT1 - 15%
* CAT2 - 15%
* Term End - 30%
* Internals - 40%

The grades used in the project are:

| Score        | Grade |
| ------------ | ----- |
| 90 and above | S     |
| 80 - 89.99   | A     |
| 70 - 79.99   | B     |
| 60 - 69.99   | C     |
| 50 - 59.99   | D     |
| 40 - 49.99   | E     |
| Below 40     | F     |

## Database

VITB360 uses SQLite as its database.

The database contains two main tables:

### Students

This table stores basic student information such as:

* Student ID
* Name
* Branch
* Semester

### Academic Records

This table stores academic information such as:

* Student ID
* Subject
* Faculty
* Slot
* Credits
* CAT1 marks
* CAT2 marks
* Term End marks
* Internal marks
* Attendance

The database file is created automatically when the program is run, so no separate database server or installation is required.

## Technologies Used

* Python 3
* SQLite
* VS Code
* Command Line / Terminal

No external Python packages are required.

## Project Files

```text
VITB360/
│
├── main.py
├── database.py
├── README.md
└── .gitignore
```

`main.py` contains the main program, menus and academic functions.

`database.py` contains the SQLite database connection and database operations.

## How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

You can check this by opening a terminal and running:

```text
python --version
```

### Step 2: Open the Project Folder

Open the project folder in VS Code or open a terminal inside the project folder.

### Step 3: Run the Program

Run:

```text
python main.py
```

The program will start in the terminal.

### Step 4: Use the Menu

Choose one of the available user types:

```text
1. Administrator
2. Faculty
3. Student
4. Exit
```

Follow the instructions shown by the program.

## Database Setup

There is no separate database setup required.

When `main.py` is run for the first time, the program automatically creates the SQLite database and the required tables.

## Notes

This project was developed as a beginner-level Python project with a focus on functions, lists, dictionaries, menu-driven programming and basic SQL/database connectivity.

The aim was to keep the system simple enough to understand while still making it useful as an academic record and performance management system.
