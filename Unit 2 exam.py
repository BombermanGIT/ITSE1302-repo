#!/usr/bin/env python3

import random


def create_employee(employee_list, employee_id, employee_name):
    while True:
        name = input("Enter the employee's name: ").strip()

        name_exists = any(
            name.casefold() == existing.casefold()
            for existing in employee_name
        )
        name_in_log = any(
            name.casefold() == employee["name"].casefold()
            for employee in employee_list
        )

        if name and not name_exists and not name_in_log:
            break

        if not name:
            print("Do not leave name blank.")
        else:
            print("Employee is already in the log.")

    employee_name.append(name)

    employee_id_number = random.randint(1, 500)
    while employee_id_number in employee_id:
        employee_id_number = random.randint(1, 500)

    employee_id.append(employee_id_number)

    employee = {"name": name, "ID": employee_id_number}
    employee_list.append(employee)


def output_employee(employee):
    output_string = (
        f"New employee: {employee['name']} "
        f"(ID: {employee['ID']})"
    )
    print(output_string)


def main():
    print(
        "Random Organization Log. The purpose of this code is to make a log "
        "of new and existing employees."
    )
    print()

    employee_list = []
    employee_id = []
    employee_name = []

    while True:
        try:
            amount = int(input("How many new employees are being added? "))
            if amount >= 0:
                break
            print("Please enter zero or a positive number.")
        except ValueError:
            print("Please enter a whole number.")

    for _ in range(amount):
        create_employee(employee_list, employee_id, employee_name)

    print("\nCreated employee details:")
    for employee in employee_list:
        output_employee(employee)

    print("\nEmployee list:")
    print(employee_list)

    print("Completed by, Daniel Brown")


if __name__ == "__main__":
    main()
