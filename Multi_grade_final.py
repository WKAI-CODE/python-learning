# Grade Calculator Program
# Author: Kai Cheng
# Description: A Python program that calculates grades based on score input.
# Created while learning Python programming fundamentals.

def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


def get_student_count():
    while True:
        try:
            count = int(input("How many students? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if count <= 0:
            print("Please enter a number greater than 0.")
            continue

        return count


def get_mark(student_number):
    while True:
        try:
            mark = int(input(f"Enter mark for student {student_number} (0-100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if mark < 0 or mark > 100:
            print("Invalid mark! Enter (0-100).")
            continue

        return mark


def save_results(filepath, students):
    if len(students) == 0:
        with open(filepath, "w") as file:
            file.write("No students in the system.\n")
        return
    
    average, highest, lowest, class_grade = calculate_summary(students)

    with open(filepath, "w") as file: 
            file.write("--- Grade Summary ---\n")
            file.write(f"Total students: {len(students)}\n")
            file.write(f"Average mark: {average:.2f}\n")
            file.write(f"Highest mark: {highest}\n")
            file.write(f"Lowest mark: {lowest}\n")

            file.write("\nStudent Records:\n")
            for s in students:
                file.write(f"{s['name']} - {s['mark']} ({s['grade']})\n")

            file.write(f"\nClass Grade: {class_grade}\n")


def search_student(students, target_name):
    for student in students:
        if student["name"].lower() == target_name.lower():
            return student
    
    return None


def edit_student_mark(students, target_name):
    for student in students:
        if student["name"].lower() == target_name.lower():
            while True:
                try:
                    new_mark = int(input(f"Enter new mark for {student["name"]} (0-100): "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if new_mark < 0 or new_mark > 100:
                    print("Invalid mark! Enter 0-100.")
                    continue
 
                student["mark"] = new_mark
                student["grade"] = get_grade(new_mark)
                return student
            
    return None
    

def calculate_summary(students):
    marks=[student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    class_grade = get_grade(average)

    return average, highest, lowest, class_grade


def delete_student(students, target_name):
    for i, student in enumerate(students):
        if student["name"].lower() == target_name.lower():
            removed_student = students.pop(i)
            return removed_student
    
    return None


def show_summary(students):
    if len(students) == 0:
        print("No students in the system.")
        return
    
    average, highest, lowest, class_grade = calculate_summary(students)

# Summary
    print("\n--- Summary ---")
    print(f"Total students: {len(students)}")
    print(f"Average mark: {average:.2f}")
    print(f"Highest mark: {highest}")
    print(f"Lowest mark: {lowest}")
    print(f"Class Grade: {class_grade}")

# Student Record 
    print("\nStudent Record: ")
    for s in students:
        print(f"ID {s['id']} | {s['name']} - {s['mark']} ({s['grade']})")


def grade_distribution(students):
    grades = [student["grade"] for student in students]

    grade_counts = {}

    for grade in grades:
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    print("\n--- Grade Distribution ---")

    total = len(students)

    for grade in ["A", "B", "C", "D", "F"]:
        count = grade_counts.get(grade, 0)
        percentage = (count / total) * 100
        print(f"{grade}: {count} students ({percentage:.0f}%)")


def main():
    count = get_student_count()
    
    students = []
    for student_number in range(1, count + 1):
        while True:
            name = input(f"Enter name for student {student_number}: ")

            if any (s["name"].lower() == name.lower() for s in students):
                print("Student name already exists. Please enter a different name.")
                continue
            
            break

        mark = get_mark(student_number)
        grade = get_grade(mark)

        students.append({
            "id": student_number,
            "name": name,
            "mark": mark,
            "grade": grade
        })
        
        print(f"{name}: {mark} -> Grade {grade}")
        
    while True:
        print("\n--- Student Grade System Menu ---")
        print("1. Show summary")
        print("2. Search student")
        print("3. Edit student mark")
        print("4. Delete student")
        print("5. Show top students")
        print("6. Save results to file")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_summary(students)
            grade_distribution(students)

        
        elif choice == "2":
            search_name = input("Enter a student name to search: ")
            result = search_student(students, search_name)
            
            if result:
                print(f"Found: {result['name']} - {result['mark']} ({result['grade']})")
            else:
                print("Student not found.")


        elif choice  == "3":
            edit_name = input("Enter a student name to edit mark: ")
            updated_student = edit_student_mark(students, edit_name)
            
            if updated_student:
                print(f"Updated: {updated_student['name']} - {updated_student['mark']}({updated_student['grade']})")
            else:
                print("Student not found.")


        elif choice == "4":
            delete_name = input("Enter a student name to delete: ")
            confirm = input(f"Are you sure you want to delete {delete_name}? (y/n): ").lower()
            
            if confirm == "y":
                deleted_student = delete_student(students, delete_name)

                if deleted_student:
                    print(f"Deleted: {deleted_student['name']} - {deleted_student['mark']} ({deleted_student['grade']})")
                else:
                    print("Student not found.")
            else:
                print("Deletion cancelled.")

        elif choice == "5":
            if len(students) == 0:
                print("No students in the system.")
            else:
                sorted_students = sorted(students, key=lambda s: s ["mark"], reverse=True)

                print("\n--- Top Students ---")
                
                for i, student in enumerate(sorted_students[:3], start=1):
                    print(f"{i}. {student['name']} - {student['mark']}")


        elif choice == "6":
            # Output Save in File  
            filepath = "result.txt"
            save_results(filepath, students)
            print("\nResult saved to result.txt successfully")


        elif choice == "7":
            print("Program ended.")
            break


        else:
            print("Invalid choice. Please enter 1 to 7.")

if __name__ == "__main__":

    main()
