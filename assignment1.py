#!python3
"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

initial = float(input("What is the initial investment?: "))
ir = float(input("What is the annual interest rate(Percentage)?: "))
ir=(ir/100)
time = float(input("How long?: "))
unit = input("Years, Months, or Days?: ")

if unit == "Months" or "months":
  time/=12
  print(f"{initial}*{ir}*{time} = {initial*ir*time}$ earned")
elif unit == "Years" or "years":
  print(f"{initial}*{ir}*{z} = {initial*ir*time}$ earned")
elif unit == "Days" or "days":
  time/=365
  print(f"{initial}*{ir}*{z} = {initial*ir*time}$ earned")
else:
  print("you did not imput the numbers correctly somehow :(")