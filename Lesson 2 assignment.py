#!/usr/bin/env python3

# display title
print("Lesson 2 Assignment")
print()
# name entry
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
# current year and birth year entry
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))
# calcuate age
user_age = current_year - birth_year
print()
print("Hello,", first_name + " " + last_name + "!\nYou are " + str(user_age) + " years old.")
print()
# Assignment operator to add a number to the user_age and displays result.
print(f"In the next year 2027, you will be {user_age + 1} years old.")
print()
print("------------------")
print("Written by, Daniel brown")
