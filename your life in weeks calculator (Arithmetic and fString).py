# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_in_months = int(age) * 12
age_in_weeks = int(age) * 52
age_in_days = int(age) * 365

months_left = 90 * 12 - age_in_months
weeks_left = 90 * 52 - age_in_weeks
days_left = 90 * 365 - age_in_days

#If we assume we live up to 90, then
#code the print statement into a variable for cleaner looking good
message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left"
print(message)

