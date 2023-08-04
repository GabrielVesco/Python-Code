print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You arrive at the famous island where the treasure is hidden. There are two paths infront of you. Which way do you go?")
first_move = input("Do you want to go left or right? \n")
first_move = first_move.lower()

if first_move == "right":
  print("You cross paths with some space pirates and they shoot you with space cannons. Game Over.")
elif first_move == "left":
  print("You choose to go left and you come across a river.")
  print("It's mating season and there are many alligators swimming in the river, but you think you are a capable swimmer and can get past them.")
  second_move = input('Do you want to swim across or wait until the alligators fall asleep? Type "swim" to swim or "wait" to wait. \n')
  second_move = second_move.lower()
  if second_move == "swim":
    print("You fool! The alligators see you in their territory and eat you alive. Game Over.")
  elif second_move == "wait":
    print("You wait until the alligators fall asleep. You safely cross the river.")
    print("While swimming across, you're pulled under by a mysterious force. You almost drown but you find yourself in a hidden cave underwater, with three mysterious doors infront of you.")
    third_move = input("Which door do you want to enter through? Red, yellow, or blue? \n")
    third_move = third_move.lower()
    if third_move == "red":
      print("A giant boulder comes swinging down through the door and crushes you. Game over.")
    elif third_move == "blue":
      print("Poisonous arrows shoot from the walls in every direction. You are hit and die a slow and painful death. Game Over.")
    elif third_move == "yellow":
      print("You open the yellow door and lo and behold you find yourself in a room with a mountain of treasure. You win!")
      print('''
  ______________________________________________________________________
 |.============[_F_E_D_E_R_A_L___R_E_S_E_R_V_E___N_O_T_E_]=============.|
 ||%&%&%&%_    _        _ _ _   _ _  _ _ _     _       _    _  %&%&%&%&||
 ||%&.-.&/||_||_ | ||\||||_| \ (_ ||\||_(_  /\|_ |\|V||_|)|/ |\ %&.-.&&||
 ||&// |\ || ||_ \_/| ||||_|_/ ,_)|||||_,_) \/|  ||| ||_|\|\_|| &// |\%||
 ||| | | |%               ,-----,-'____'-,-----,               %| | | |||
 ||| | | |&% """"""""""  [    .-;"`___ `";-.    ]             &%| | | |||
 ||&\===//                `).'' .'`_.- `. '.'.(`  A 76355942 J  \\===/&||
 ||&%'-'%/1                // .' /`     \    \\                  \%'-'%||
 ||%&%&%/`   d8888b       // /   \  _  _;,    \\      .-"""-.  1 `&%&%%||
 ||&%&%&    8P |) Yb     ;; (     > a  a| \    ;;    //A`Y A\\    &%&%&||
 ||&%&%|    8b |) d8     || (    ,\   \ |  )   ||    ||.-'-.||    |%&%&||
 ||%&%&|     Y8888P      ||  '--'/`  -- /-'    ||    \\_/~\_//    |&%&%||
 ||%&%&|                 ||     |\`-.__/       ||     '-...-'     |&%&%||
 ||%%%%|                 ||    /` |._ .|-.     ||                 |%&%&||
 ||%&%&|  A 76355942 J  /;\ _.'   \  } \  '-.  /;\                |%&%&||
 ||&%.-;               (,  '.      \  } `\   \'  ,)   ,.,.,.,.,   ;-.%&||
 ||%( | ) 1  """""""   _( \  ;...---------.;.; / )_ ```""""""" 1 ( | )%||
 ||&%'-'==================\`------------------`/=================='-'%&||
 ||%&%&%&%&%&%&%%&%&&&%&%%&)O N E  D O L L A R(%&%&%&%&%&%&%%&%&&&%&%%&||
 ||%JGS%&%&%&%&%&%&%&%&%&&/_.----------------._\%&%&%%&%&&%%&%&%&%&%&%&||
 '""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""`
 ''')
    else:
      print("Invalid entry.")
  else:
    print("Invalid entry.")
else:
  print("Invalid entry.")


