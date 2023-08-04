#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#list of letters
letters_list = []
for n in range(1,nr_letters+1):
  letter = random.choice(letters)
  letters_list.append(letter)

#list of numbers
numbers_list = []
for n in range(1,nr_numbers+1):
  number = random.choice(numbers)
  numbers_list.append(number)

#list of symbols
symbols_list = []
for n in range(1,nr_symbols+1):
  symbol = random.choice(symbols)
  symbols_list.append(symbol)

#now we concatenate them together!
total_characters = len(letters_list) + len(numbers_list) + len(symbols_list)
character_list = letters_list + numbers_list + symbols_list

#create our list of randomly ordered characters
random_list = random.sample(range(1,total_characters + 1), total_characters)

#now we loop through our character list following the order of the random_list
new_password = []
for n in random_list:
  character = character_list[n-1]
#  new_password.append(character) (either works!)
  new_password += character

#formatting
print("".join(new_password))

#done!

