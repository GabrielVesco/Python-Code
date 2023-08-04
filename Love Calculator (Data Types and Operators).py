# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

letter_T = name1.count("t") + name2.count("t")
letter_R = name1.count("r") + name2.count("r")
letter_U = name1.count("u") + name2.count("u")
letter_E = name1.count("e") + name2.count("e")

letter_L = name1.count("l") + name2.count("l")
letter_O = name1.count("o") + name2.count("o")
letter_V = name1.count("v") + name2.count("v")
#we already have letter E

true_total = letter_T + letter_R + letter_U + letter_E
love_total = letter_L + letter_O + letter_V + letter_E

love_score = str(true_total) + str(love_total)
love_score = int(love_score)

#Or simply wrap
#love_score = int(str(true_total) + str(love_total))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")