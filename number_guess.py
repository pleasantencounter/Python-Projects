#!/usr/bin/python
import random

num = 0
count = 0

for i in range(1,5):
    count +=25
    print(f"({i}) Guess a number between 1 and {count}")

level = int(input("Choose level: "))

if level == 1:
    rand_num = random.randint(1,25)
elif level == 2:
    rand_num = random.randint(1,50)
elif level == 3:
    rand_num = random.randint(1,100)
else:
    print("You did not choose a level between 1 and 3 ")
    exit(1)

count = 0
while num != rand_num and count < 5:
    num = int(input("Enter a number: "))
    count +=1
    if num > rand_num:
        print("Try a smaller number")      
    elif num < rand_num:
        print("Try a bigger number")
    elif num == rand_num:
        print(f"Nice job you guessed it: {rand_num}")
    
if num != rand_num and count == 5:
    print(f"Sorry you only have 5 guesses!")
    print(f"The number was {rand_num}")
