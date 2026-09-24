students = {}

while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        students[name] = marks
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students added yet.")
        else:
            for name, marks in students.items():
                if marks >= 90:
                    grade = "A"
                elif marks >= 75:
                    grade = "B"
                elif marks >= 60:
                    grade = "C"
                elif marks >= 40:
                    grade = "D"
                else:
                    grade = "F"

                print(f"{name}: {marks} - Grade {grade}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")