#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
#updated to current tipping suggestions nowadays 
tip_percentage = float(input("What percentage would you like to give? 15, 18, or 20? "))
people_to_split = float(input("How many people to split the bill? "))

#calculating the bill per person based on given inputs
bill_per_person = total_bill * (1 + tip_percentage/100) / people_to_split

#next we round the result to 2 decimals because it's currency
#bill_per_person = round(bill_per_person, 2)

#update - do not simply use round(,2) since it will not print
# a 0 if the bill ends with a 0 on the cents

#use formats instead
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"${bill_per_person}")