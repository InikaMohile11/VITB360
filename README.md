# VITB360: STUDENT ACADEMIC AND PERFORMANCE HUB

## About the Project

VITB360 is a simple command-line based academic management system developed using Python and SQLite.

The project started as a basic student-record system and was expanded into an academic hub with student management, subject records, marks, attendance, performance insights, achievements and a What-If Grade Simulator.

The system provides separate menus for three types of users:

* Administrator
* Faculty
* Student

---

## Features

### Administrator

* Add student records
* View student records
* Search for students
* Update student information
* Delete student records
* Add subjects
* Store faculty, slot and credit details

### Faculty

* View student records
* Add CAT1 marks
* Add CAT2 marks
* Add Term End marks
* Add Internal marks
* Add Attendance

### Student

* View academic dashboard
* View subject-wise performance
* View average score
* View attendance
* View strongest subject
* View academic highlights
* View Achievement Wall
* Use What-If Grade Simulator

---

## Academic Score Calculation

The final score is calculated using the following weightage:

| Component | Weightage |
| --------- | --------: |
| CAT1      |       15% |
| CAT2      |       15% |
| Term End  |       30% |
| Internals |       40% |

### Grade System

| Score        | Grade |
| ------------ | ----- |
| 90 and above | S     |
| 80 – 89.99   | A     |
| 70 – 79.99   | B     |
| 60 – 69.99   | C     |
| 50 – 59.99   | D     |
| 40 – 49.99   | E     |
| Below 40     | F     |

---

## Database

VITB360 uses SQLite for persistent storage.

The database contains two main tables:

### Students

Stores:

* Student ID
* Name
* Branch
* Semester

### Academic Records

Stores:

* Student ID
* Subject Name
* Faculty
* Slot
* Credits
* CAT1 marks
* CAT2 marks
* Term End marks
* Internal marks
* Attendance

The SQLite database file is created automatically when the application is run.

---

## Technologies Used

* Python 3
* SQLite
* Command-Line Interface (CLI)
* GitHub

No external Python packages are required.

---

## Project Files

```text
VITB360/
│
├── main.py
├── database.py
├── test_project.py
├── README.md
├── statement.md
└── .gitignore
```

### File Description

**main.py**
Contains the main application, menus and academic features.

**database.py**
Contains SQLite database connection and database operations.

**test_project.py**
Contains basic tests for score calculation and grade calculation.

**README.md**
Contains project documentation, features and instructions.

**statement.md**
Contains the problem statement, project scope, target users and high-level features.

**.gitignore**
Prevents generated files such as the SQLite database and Python cache files from being uploaded.

---

## How to Run

### Requirements

* Python 3 installed on your computer
* Command Prompt, PowerShell or any Python-supported terminal

### Steps

1. Download or clone the repository.

2. Open the project folder in a terminal.

3. Run the application:

```text
python main.py
```

4. The VITB360 main menu will appear.

5. Select the required user role and follow the menu options.

---

## Database Setup

No separate database installation is required.

When the application starts, the required SQLite tables are created automatically.

The database file is stored locally as:

```text
vitb360.db
```

This file is ignored by Git using `.gitignore`.

---

## Testing

Basic testing is provided through `test_project.py`.

Run:

```text
python test_project.py
```

The tests verify:

* Score calculation
* Grade calculation
* Grade boundary logic

---

## Notes

* VITB360 is a command-line based application.
* The project uses basic Python concepts such as functions, lists, dictionaries, loops and conditional statements.
* SQLite is used for local persistent storage.
* The project is designed as a first-year academic programming project.
* No external Python libraries are required.
