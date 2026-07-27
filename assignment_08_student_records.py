# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
# =============================================================================


def print_menu():
    """Display the main menu."""
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def calculate_average(scores):
    """Return the average of a list of scores, rounded to 2 decimal places."""
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)


def add_student(students):
    """Prompt for a student's details and add them to the list of records."""
    name = input("Student name: ")
    student_id = input("Student ID: ")

    try:
        num_scores = int(input("How many scores? "))
    except ValueError:
        print("Error: please enter a valid number of scores.")
        return

    if num_scores <= 0:
        print("Error: number of scores must be positive.")
        return

    scores = []
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score {i + 1}: "))
                scores.append(score)
                break
            except ValueError:
                print("Error: please enter a valid number.")

    student = {
        "name": name,
        "id": student_id,
        "scores": scores,
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Print a formatted table of every student's name, ID, scores, average."""
    if not students:
        print("No students have been added yet.")
        return

    line = "-" * 50
    print(line)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print(line)

    for student in students:
        scores_text = ", ".join(str(int(s)) if s == int(s) else str(s) for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_text:<15}{average:<10}")

    print(line)


def find_student_by_id(students, student_id):
    """Return the student dict matching student_id, or None if not found."""
    for student in students:
        if str(student["id"]) == str(student_id):
            return student
    return None


def show_average_for_student(students):
    """Ask for a student ID and display that student's average score."""
    student_id = input("Enter student ID: ")
    student = find_student_by_id(students, student_id)

    if student is None:
        print(f"Error: no student found with ID {student_id}.")
        return

    average = calculate_average(student["scores"])
    print(f"{student['name']}'s average score: {average}")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            show_average_for_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: please enter a number from 1 to 4.")

        print()


if __name__ == "__main__":
    main()