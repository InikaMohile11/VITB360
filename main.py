import database
print("======================================")
print("VITB360: STUDENT ACADEMIC AND PERFORMANCE HUB")
print("======================================")

students = []
def load_students():
    data = database.get_students_db()

    for row in data:
        student = {
            "id": row[0],
            "name": row[1],
            "branch": row[2],
            "semester": row[3],
            "subjects": {}
        }

        students.append(student)


def add_student():
    student_id = input("Enter Student ID: ")
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    semester = input("Enter Semester: ")

    student = {
        "id": student_id,
        "name": name,
        "branch": branch,
        "semester": semester,
        "subjects": {}
    }

    students.append(student)
    database.add_student_db(student_id, name, branch, semester)
    print("Student added successfully!")
    print("Student record saved to database.")


def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("Student Records:")

        for student in students:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Semester:", student["semester"])
            print("Subjects:")

            for subject_name in student["subjects"]:
                subject = student["subjects"][subject_name]

                print("  Subject Name:", subject_name)
                print("    Faculty:", subject["faculty"])
                print("    Slot:", subject["slot"])
                print("    Credits:", subject["credits"])
                print("    CAT1 Marks:", subject["cat1"])
                print("    CAT2 Marks:", subject["cat2"])
                print("    Term Exam Marks:", subject["term_end"])
                print("    Internals Marks:", subject["internals"])
                print("    Attendance:", subject["attendance"])

                score = calculate_score(subject)
                print("    Weighted Score:", round(score, 2))

                grade = calculate_grade(score)
                print("    Grade:", grade)
                print("--------------------")


def search_student():
    search_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == search_id:
            print("Student Found:")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Semester:", student["semester"])
            return

    print("Student not found.")


def update_student():
    update_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == update_id:
            print("Student Found. Enter new details:")

            new_name = input("Enter New Name: ")
            new_branch = input("Enter New Branch: ")
            new_semester = input("Enter New Semester: ")

            student["name"] = new_name
            student["branch"] = new_branch
            student["semester"] = new_semester
            database.update_student_db(
                update_id,
                new_name,
                new_branch,
                new_semester
            )

            print("Student record updated successfully!")
            return

    print("Student not found.")


def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            database.delete_student_db(delete_id)
            print("Student record deleted successfully!")
            return

    print("Student not found.")


def add_subject():
    student_id = input("Enter Student ID to add subject: ")

    for student in students:
        if student["id"] == student_id:

            subject_name = input("Enter Subject Name: ")
            if subject_name in student["subjects"]:
                print("Subject already exists for the student.")
                return
            faculty = input("Enter Faculty Name: ")
            slot = input("Enter Slot: ")
            credits = input("Enter Credits: ")

            subject = {
                "faculty": faculty,
                "slot": slot,
                "credits": credits,
                "cat1": 0,
                "cat2": 0,
                "term_end": 0,
                "internals": 0,
                "attendance": 0
            }

            student["subjects"][subject_name] = subject

            database.add_academic_record(
                student_id,
                subject_name,
                faculty,
                slot,
                credits
            )
            print("Subject added successfully!")
            return

    print("Student not found.")


def add_cat1():
    student_id = input("Enter Student ID to add CAT1 marks: ")

    for student in students:
        if student["id"] == student_id:

            subject_name = input("Enter Subject Name to add CAT1 marks: ")

            if subject_name in student["subjects"]:
                cat1 = input("Enter CAT1 Marks: ")
                student["subjects"][subject_name]["cat1"] = cat1
                database.update_cat1(student_id, subject_name, cat1)

                print("CAT1 marks added successfully!")
                return
            else:
                print("Subject not found for the student.")
                return

    print("Student not found.")


def add_cat2():
    student_id = input("Enter Student ID to add CAT2 marks: ")

    for student in students:
        if student["id"] == student_id:

            subject_name = input("Enter Subject Name to add CAT2 marks: ")

            if subject_name in student["subjects"]:
                cat2 = input("Enter CAT2 Marks: ")
                student["subjects"][subject_name]["cat2"] = cat2
                database.update_cat2(student_id, subject_name, cat2)

                print("CAT2 marks added successfully!")
                return
            else:
                print("Subject not found for the student.")
                return

    print("Student not found.")


def add_term_end():
    student_id = input("Enter Student ID to add Term End marks: ")

    for student in students:
        if student["id"] == student_id:

            subject_name = input("Enter Subject Name to add Term End marks: ")

            if subject_name in student["subjects"]:
                term_end = input("Enter Term End Marks: ")
                student["subjects"][subject_name]["term_end"] = term_end
                database.update_term_end(student_id, subject_name, term_end)
                print("Term End marks added successfully!")
                return
            else:
                print("Subject not found for the student.")
                return

    print("Student not found.")


def add_internals():
    student_id = input("Enter Student ID to add Internals marks: ")

    for student in students:
        if student["id"] == student_id:

            subject_name = input("Enter Subject Name to add Internals marks: ")

            if subject_name in student["subjects"]:
                internals = input("Enter Internals Marks: ")
                student["subjects"][subject_name]["internals"] = internals
                database.update_internals(student_id, subject_name, internals)
                print("Internals marks added successfully!")
                return
            else:
                print("Subject not found for the student.")
                return

    print("Student not found.")


def add_attendance():
    student_id = input("Enter Student ID to add Attendance: ")

    for student in students:
        if student["id"] == student_id:

            subject_name = input("Enter Subject Name to add Attendance: ")

            if subject_name in student["subjects"]:
                attendance = input("Enter Attendance Percentage: ")
                student["subjects"][subject_name]["attendance"] = attendance
                database.update_attendance(student_id, subject_name, attendance)   
                print("Attendance added successfully!")
                return
            else:
                print("Subject not found for the student.")
                return

    print("Student not found.")


def calculate_score(subject):
    cat1 = float(subject["cat1"])
    cat2 = float(subject["cat2"])
    term_end = float(subject["term_end"])
    internals = float(subject["internals"])

    score = (cat1 * 15 / 100) + (cat2 * 15 / 100) + \
            (term_end * 30 / 100) + (internals * 40 / 100)

    return score


def calculate_grade(score):
    if score >= 90:
        return "S"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


def dashboard_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            return student

    return None


def student_dashboard():
    student = dashboard_student()

    if student is None:
        print("Student not found.")
        return

    print("\n======================================")
    print("          STUDENT DASHBOARD")
    print("======================================")

    print("Name:", student["name"])
    print("Branch:", student["branch"])
    print("Semester:", student["semester"])

    print("--------------------------------------")

    total_score = 0
    total_attendance = 0
    subject_count = 0

    highest_score = 0
    highest_subject = ""

    for subject_name in student["subjects"]:
        subject = student["subjects"][subject_name]
        score = calculate_score(subject)
        attendance = float(subject["attendance"])

        total_score = total_score + score
        total_attendance = total_attendance + attendance
        subject_count = subject_count + 1

        if score > highest_score:
            highest_score = score
            highest_subject = subject_name

    if subject_count > 0:
        average = total_score / subject_count
        average_attendance = total_attendance / subject_count

        print("Academic Average:", round(average, 2))
        print("Average Attendance:", round(average_attendance, 2), "%")

        print("\nSUBJECT PERFORMANCE")

        for subject_name in student["subjects"]:
            subject = student["subjects"][subject_name]
            score = calculate_score(subject)
            grade = calculate_grade(score)

            print(subject_name, ":", round(score, 2), "- Grade", grade)

        print("\n--------------------------------------")
        print("YOUR HIGHLIGHTS")
        print("--------------------------------------")

        print("Strongest Subject:", highest_subject)

        if average >= 90:
            print("Performance: Excellent!")
        elif average >= 80:
            print("Performance: Very Good!")
        elif average >= 70:
            print("Performance: Good!")
        elif average >= 60:
            print("Performance: On Track")
        else:
            print("Performance: Needs Attention")

        if average_attendance >= 90:
            print("Attendance: Excellent")
        elif average_attendance >= 75:
            print("Attendance: Good")
        else:
            print("Attendance: Needs Attention")

        print("\nTODAY'S HIGHLIGHT")

        if average >= 90:
            print("You are performing at an excellent level!")
        elif highest_subject != "":
            print("Your strongest subject is", highest_subject + "!")
        else:
            print("Keep working and build your academic record!")

    else:
        print("No subjects found for this student.")


def achievement_wall():
    student = dashboard_student()

    if student is None:
        print("Student not found.")
        return

    total_score = 0
    total_attendance = 0
    subject_count = 0

    for subject_name in student["subjects"]:
        subject = student["subjects"][subject_name]

        score = calculate_score(subject)
        attendance = float(subject["attendance"])

        total_score = total_score + score
        total_attendance = total_attendance + attendance
        subject_count = subject_count + 1

    if subject_count == 0:
        print("No academic records found.")
        return

    average = total_score / subject_count
    average_attendance = total_attendance / subject_count

    print("\n======================================")
    print("           ACHIEVEMENT WALL")
    print("======================================")

    achievement_found = False

    if average >= 90:
        print("TOP PERFORMER")
        achievement_found = True

    if average >= 75:
        print("CONSISTENT LEARNER")
        achievement_found = True

    if average_attendance >= 90:
        print("ATTENDANCE STAR")
        achievement_found = True

    if average >= 80 and average_attendance >= 85:
        print("ALL-ROUNDER")
        achievement_found = True

    for subject_name in student["subjects"]:
        subject = student["subjects"][subject_name]

        if float(subject["cat2"]) > float(subject["cat1"]):
            print("RISING STAR -", subject_name)
            achievement_found = True

    if achievement_found == False:
        print("Keep going! Your first achievement is waiting.")


def what_if_grade():
    student = dashboard_student()

    if student is None:
        print("Student not found.")
        return

    subject_name = input("Enter Subject Name: ")

    if subject_name not in student["subjects"]:
        print("Subject not found.")
        return

    subject = student["subjects"][subject_name]

    print("\n======================================")
    print("       WHAT-IF GRADE SIMULATOR")
    print("======================================")

    cat1 = float(subject["cat1"])
    internals = float(subject["internals"])

    print("Current CAT1 Marks:", cat1)
    print("Current Internals:", internals)

    cat2 = float(input("Enter Expected CAT2 Marks: "))
    term_end = float(input("Enter Expected Term End Marks: "))

    projected_score = (cat1 * 15 / 100) + (cat2 * 15 / 100) + \
                      (term_end * 30 / 100) + (internals * 40 / 100)

    print("\n--------------------------------------")
    print("Projected Weighted Score:", round(projected_score, 2))
    print("Projected Grade:", calculate_grade(projected_score))
    print("--------------------------------------")

    if projected_score >= 90:
        print("You are on track for an S grade!")
    elif projected_score >= 80:
        print("You are on track for an A grade!")
    elif projected_score >= 70:
        print("You are on track for a B grade!")
    else:
        print("Keep working towards improving your score!")


def admin_menu():
    while True:
        print("\n========== ADMINISTRATOR ==========")
        print("1. Add Student")
        print("2. View Student Records")
        print("3. Search Student")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Add Subject for Student")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            add_subject()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


def faculty_menu():
    while True:
        print("\n========== FACULTY ==========")
        print("1. View Student Records")
        print("2. Add CAT1 Marks")
        print("3. Add CAT2 Marks")
        print("4. Add Term End Marks")
        print("5. Add Internals Marks")
        print("6. Add Attendance")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_students()
        elif choice == "2":
            add_cat1()
        elif choice == "3":
            add_cat2()
        elif choice == "4":
            add_term_end()
        elif choice == "5":
            add_internals()
        elif choice == "6":
            add_attendance()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


def student_menu():
    while True:
        print("\n========== STUDENT ==========")
        print("1. Student Dashboard")
        print("2. Achievement Wall")
        print("3. What-If Grade Simulator")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_dashboard()
        elif choice == "2":
            achievement_wall()
        elif choice == "3":
            what_if_grade()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def main_menu():
    while True:
        print("\n======================================")
        print("              VITB360")
        print("======================================")

        print("1. Administrator")
        print("2. Faculty")
        print("3. Student")
        print("4. Exit")

        choice = input("Select User Type: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            faculty_menu()
        elif choice == "3":
            student_menu()
        elif choice == "4":
            print("Thank you for using VITB360. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    database.create_table()  
    database.create_academic_table()
    load_students()
    main_menu()