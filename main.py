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
Step1=input("you are at the cross road,Where you want to go? type left or right\n")
step1_l=Step1.lower();
if(step1_l=="left"):
  Step2=input(' "you came to lake ,your treasure is middle of the island.where you need to go ? type "swim" to swim across the island or type "boat" to cross across the island " \n')
  step2_l=Step2.lower()
  if(step2_l=="boat"):
    Step3=input(' you are at the final stage of the game,there are three doors,the treasure is at any one of the door so, choose the crt door.\nWhich door you want to go type "red" or "yellow" or "blue"\n')
    step3_l=Step3.lower()
    if(step3_l=="yellow"):
      print("CONGRADULATIONS :),YOU WON THE GAME,HURRAY\n")
    else:
      print("Sorry you are at the wrong way,GAME OVER ,better luck next time")

  else:
    print("Sorry you are at the wrong way,GAME OVER ,better luck next time")

    
else:
  print("Sorry you are at the wrong way,GAME OVER ,better luck next time")
