# Data types and casting
Two_digit_number = input("Type a two digit number: ")
# print(type(Two_digit_number))
first_digit = int(Two_digit_number[0])
second_digit = int(Two_digit_number[1])
Output = first_digit + second_digit
print(Output)

# Mathematical Operations
# BMI
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
BMI = int(weight)/float(height)**2
print(int(BMI))   

# Number manipulation & F strings
age = int(input("What is your current age?"))
age_left_yrs = 90 - age
age_left_days = age_left_yrs * 365
age_left_wks = age_left_yrs * 52
age_left_mnths = age_left_yrs *12
message = f"You have {age_left_days} days, {age_left_wks} weeks, and {age_left_mnths} months left."
print(message)

# Project 2: Tip Calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percentage_tip = tip / 100
total_bill = bill * (1 + percentage_tip)
No_of_people = int(input("How many people to split the bill? "))
each_person_bill = total_bill / No_of_people
rounded_bill = round(each_perso)
output = f"Each person should pay: ${each_person_bill}"
print(output)