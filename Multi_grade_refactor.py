# Grade Calculator Program
# Author: Kai
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


def save_results(filepath, count, students, average, highest, lowest, class_grade):
    with open(filepath, "w") as file:
        file.write("--- Grade Summary ---\n")
        file.write(f"Total students: {count}\n")
        file.write(f"Average mark: {average:.2f}\n")
        file.write(f"Highest mark: {highest}\n")
        file.write(f"Lowest mark: {lowest}\n")

        file.write("\nStudent Records:\n")
        for s in students:
            file.write(f"{s['name']} - {s['mark']} ({s['grade']})\n")

        file.write(f"\nClass Grade: {class_grade}\n")


def main():
    count = get_student_count()

    students = []
    for student_number in range(1, count + 1):
        name = input(f"Enter name for student {student_number}: ")

        mark = get_mark(student_number)
        grade = get_grade(mark)

        students.append({
            "name": name,
            "mark": mark,
            "grade": grade
        })
        
        print(f"{name}: {mark} -> Grade {grade}")
    
    # Extract marks for calculations
    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    class_grade = get_grade(average)

    print("\n--- Summary ---")
    print(f"Total students: {count}")
    print(f"Average mark: {average:.2f}")
    print(f"Highest mark: {highest}")
    print(f"Lowest mark: {lowest}")
    print(f"Class Grade: {class_grade}")

    print("\nStudent Record: ")
    for s in students:
        print(f"{s['name']} - {s['mark']} ({s['grade']})")

    
    filepath = r"C:\Users\User\OneDrive\Documents\Python small exercise\Mini project 1\result.txt"
    save_results(filepath, count, students, average, highest, lowest, class_grade)

    print("\nResult saved to result.txt successfully")

if __name__ == "__main__":

    main()
