#!/usr/bin/env python3

#get input from user to start

while True:
    investment_amount = int(input("Enter the investment amount (greater than 0 and less than 50000): "))
    if investment_amount > 50000 and investment_amount < 0:
        print("The number must be more than 0 but less than 50000")
    interest_rate = int(input("Enter the interest rate (greater than 0 but less than 15): "))
    if interest_rate > 15 and interest_rate < 0:
        print("The interest rate must be greater than 0 but less than 15")
    investment_years = int(input("Enter the investment duration in years (greater than 0): "))
    if investment_years <= 0:
        print("The year entered must be greater than zero.")

    monthly_interest = interest_rate / 12 / 100
    months = investment_years * 12

    future_total = 0
    for i in range(months):
        future_total += investment_amount
        

