import time
import sys

print('************************************************************************')
print('          |                   |                  |                     |')
print(' _________|________________.=""_;=.______________|_____________________|_______')
print('|                   |  ,-"_,=""     `"=.|                  |')
print('|___________________|__"=._o`"-._        `"=.______________|___________________')
print('          |                `"=._o`"=._      _`"=._                     |')
print(' _________|_____________________:=._o "=._."_.-="\'\"=.__________________|_______')
print('|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |')
print('|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". \'__|___________________')
print('          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |')
print(' _________|___________| ;`-.o`"=._; ." ` \'`."\` . "-._ /_______________|_______')
print('|                   | |o;    `"-.o`"=._``  \'` " ,__.--o;   |')
print('|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________')
print('____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____')
print('/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/|')
print('____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____')
print('/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/')
print('____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____')
print('/______/______/______/______/______/______/______/______/______/______/')
print('*******************************************************************************\n')

print("Welcome to treasure Island!\n")
name = input("Enter your name: ")
print(f"your mission is to find the treasure, {name}\n")
print("you walk through a single silver door which leads you to another room, which has two more doors...")

choice1 = input("Which door do you choose? (left or right): ")
time.sleep(1)
if choice1 == "right":
    print(f"you fell into a hole..game over {name}")
    time.sleep(1)
    sys.exit(1)
elif choice1 == "left":
    print("you chose the correct door!")

print("you now enter a room, and in this room there are two doors...one is red and one is blue.. ")

choice2 = input("Which door do you choose? (red or blue): ")

if choice2 == "red":
    print("you chose the correct door!")
    time.sleep(1)
elif choice2 == "blue":
    print("you entered a room full of water and hungry crocodiles..goodbye..")
    time.sleep(1)
    sys.exit(1)
print("you have entered another room, this time with three doors...purple, yellow, and a gray door..")

choice3 = input("Which door do you choose? (purple, yellow, or gray): ")
time.sleep(1)
if choice3 == "purple":
    print("you chose incorrectly...you have entered a room full of venomous snakes..the door locks behind you...")
    time.sleep(1)
    sys.exit(1)
elif choice3 == "yellow":
    print("behind the yellow door lies a chainsaw wielding maniac, you are dead..")
    time.sleep(1)
    sys.exit(1)
elif choice3 == "gray":
    print("correct choice, you enter the room and find the treasure!!!")

print(f"Congrats, you have earned the dabloons and can call yourself a pirate you will be called Gold Eye {name}")
time.sleep(3)
