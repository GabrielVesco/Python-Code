rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rock_paper_or_scissors = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))

option = rock_paper_or_scissors[user_choice]

print(option)

computer_choice = random.choice(rock_paper_or_scissors)
print(f"Computer chose: \n {computer_choice}")

if option == computer_choice:
  print("It's a tie!")
else:
  if option == rock and computer_choice == scissors:
    print("You win!")
  elif option == paper and computer_choice == rock:
    print("You win!")
  elif option == scissors and computer_choice == paper:
    print("You win!")
  else:
    print("You lose")