#!/usr/bin/env python3
from random import randrange
import random

# Looking at it, adding defs at the top seemed like a good idea. Defining sorting, reversing and grade totals and averages.
def sort_grades(grades):
    grades.sort(reverse=True)


def get_total(grades):
    return sum(grades)


def get_average(grades):
    return get_total(grades) / len(grades) if grades else None


def main():
    grade_list = []
    # Start while loop for user to enter grades. The .isdigit method is fun, as it keeps people from entering decimals and negative values.
    while True:
        print("Please enter a grade or enter -1 to stop: ")
        grade_text = input().strip()

        if grade_text.isdigit() or (
            grade_text.startswith("-") and grade_text[1:].isdigit()
        ):
            grade = int(grade_text)
        else:
            print("Please enter a valid grade!")
            continue

        if grade == -1:
            break
        else:
            grade_list.append(grade)

    print(grade_list)
    # removes lowest grade
    print("Removing the lowest grade.")
    if grade_list:
        lowest_grade = min(grade_list)
        lowest_index = grade_list.index(lowest_grade)
        grade_list.pop(lowest_index)
    print(grade_list)
    # removes random grade
    print("Removing a random grade.")
    if grade_list:
        random_grade = random.choice(grade_list)
        grade_list.remove(random_grade)
    print(grade_list)

    print("Go ahead and edit the grades entered.")
    print()
    # Grade edit section. first time using if not statements.
    if grade_list:
        while True:
            for index, grade in enumerate(grade_list, start=1):
                print(f"{index}. {grade}")

            grade_number_text = input(
                "Which grade would you like to edit? "
            ).strip()

            if not grade_number_text.isdigit():
                print("Please enter valid grade from the list!")
                continue

            grade_number = int(grade_number_text)
            if grade_number < 1 or grade_number > len(grade_list):
                print("Please enter valid grade from the list!")
                continue

            while True:
                new_grades = input("Enter the new grade: ").strip()

                if new_grades.isdigit() or (
                    new_grades.startswith("-")
                    and new_grades[1:].isdigit()
                ):
                    grade_list[grade_number - 1] = int(new_grades)
                    break

                print("Please enter a valid grade!")

            break

    print(grade_list)

    print("Sorting and reversing the list of grades.")
    sort_grades(grade_list)
    print(grade_list)

    print("Adding Grade totals and average...")
    total = get_total(grade_list)
    print(f"Total: {total}")

    average = get_average(grade_list)
    if average is None:
        print("Grade Average N/A")
    else:
        print(f"Grade Average {average}")

    print("Created by, Daniel Brown.")


if __name__ == "__main__":
    main()
