student_grades = {}

# Function to add a new student and grade
def add_student():
    name = input("Enter the student's name: ")
    grade = input("Enter the student's grade: ")
    student_grades[name] = grade
    print(f"{name}'s grade has been added.")

# Function to update an existing student's grade
def update_grade():
    name = input("Enter the student's name to update the grade: ")
    if name in student_grades:
        grade = input(f"Enter the new grade for {name}: ")
        student_grades[name] = grade
        print(f"{name}'s grade has been updated.")
    else:
        print(f"Student {name} not found.")

# Function to print all student grades
def print_grades():
    if student_grades:
        print("\nAll Student Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No student grades to display.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        print_grades()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
