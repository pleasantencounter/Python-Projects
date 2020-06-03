#!/usr/bin/python
import random
choice="y"

one="""|     |  
|  x  |
|     |"""
two="""|x    |
|     |
|    x|"""
three="""|x    |
|  x  | 
|    x|"""
four="""|x   x|
|     |
|x   x|"""
five="""|x   x|
|  x  | 
|x   x|"""
six="""|x   x|
|x   x|
|x   x|"""

die_list=[one,two,three,four,five,six]

def rollDice(die):
    for i in range(1):
        print("+" + "-" * 5 + "+")
        print(die)
        print("+" +  "-" * 5 +"+")


print(" Hi! Welcome to Dicey!")
print("""

   .-------.    _______
  /   o   /|   /\\      \\
 /_______/o|  /o \\  o   \\
 | o     | | /   o\\______\\
 |   o   |o/ \\o   /o     /
 |     o |/   \\ o/  o   /
 '-------'     \\/____o_/

  """)

while choice == "y":
    die1=random.choice(die_list)
    die2=random.choice(die_list)
    input("Press enter to roll dice")
    if choice == "y":
        rollDice(die1)
        print(" ")
        rollDice(die2)
        choice = str(input("Would you like to continue y/n?"))
    else:
        print("Thanks for playing!")
