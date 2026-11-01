#!/usr/bin/env python3
def main():
    student_information = {}
    # creating empty dictionary and fillign it with the contents for the lesson.
    student_information["Resurrection Joe"] = {
        "ID": 1,
        "GPA": 3.5,
        "credits completed": 77.0,
        "grades": [100, 88, 75, 90]
    }

    student_information["Rosa Morgue"] = {
        "ID": 2,
        "GPA": 3.8,
        "credits completed": 36.0,
        "grades": [100, 90, 87, 92]
    }

    print(student_information)
    print()
    print("List of students:")
    # printing list of student names.
    for student_name in student_information:
        print(student_name)

    print()
    print("Accessing student information")
    print("Name\tID\tGPA\tCredits Completed\tGrades")
    # a for loop to pull information and make it into a faux table. That I cannot figure out to make uniform.
    for name, information in student_information.items():
        print(
            f"{name}\t"
            f"{information['ID']}\t"
            f"{information['GPA']}\t"
            f"{information['credits completed']}\t"
            f"{information['grades']}"
        )

    print()
    print("The list has changed! Updating...")
    # removing a student because they DEAD.
    student_information.pop("Resurrection Joe")
    print("Resurrection Joe failed to resurrect and is no longer attending classes!")

    print(student_information)
    print()
    # listing GPA of who remains in the dictionary.
    for name, information in student_information.items():
        gpa = information.get("GPA")
        print(f"{name}'s GPA is: {gpa}")

    print()
    # Clearing the dictionary.
    print("The list has changed! Updating...")
    student_information.clear()
    print(student_information)
    print("It seems everyone is gone!")
    print()
    print("Completed by, Daniel Brown")


if __name__ == "__main__":
    main()
