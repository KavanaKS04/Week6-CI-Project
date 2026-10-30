def calculate_average(marks):
    if not marks:
        raise ValueError("At least one mark is required.")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100.")

    return sum(marks) / len(marks)


def get_grade(average):
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100.")

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def generate_report(student_name, marks):
    if not student_name.strip():
        raise ValueError("Student name cannot be empty.")

    average = calculate_average(marks)
    grade = get_grade(average)

    return {
        "name": student_name.strip(),
        "average": round(average, 2),
        "grade": grade
    }


def main():
    print("STUDENT MARKS CALCULATOR")

    name = input("Enter student name: ")

    try:
        marks_input = input("Enter marks separated by spaces: ")
        marks = [float(mark) for mark in marks_input.split()]

        report = generate_report(name, marks)

        print("\nStudent Name:", report["name"])
        print("Average Marks:", report["average"])
        print("Grade:", report["grade"])

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
