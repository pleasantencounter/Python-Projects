#!/usr/bin/python
import random

item = ['Rock', 'Paper','Scissors']
cpupoints = 0
userpoints = 0

while True:

	if cpupoints == 3:
		print("CPU wins!")
		break

	elif userpoints == 3:
		print("User wins!")
		break

	else:

		userinput = (input("Enter 'r' for Rock, 'p' for Paper or 's' for Scissors: ").lower())
		randomItem = random.choice(item)

		if userinput == 'r' or userinput == 'p' or userinput == 's':

			if(randomItem == 'Rock' and userinput == 'r'):
				print("It's a tie")
			elif(randomItem == 'Paper' and userinput == 'p'):
				print("It's a tie")
			elif(randomItem == 'Scissors' and userinput == 's'):
				print("It's a tie")
			elif(randomItem == 'Rock' and userinput == 's'):
				if(item[0]):
					cpupoints = cpupoints + 1
			elif(randomItem == 'Rock' and userinput == 'p'):
				if(item[0]):
					userpoints = userpoints + 1
			elif(randomItem == 'Paper' and userinput == 's'):
				if(item[1]):
					userpoints = userpoints + 1
			elif(randomItem == 'Paper' and userinput == 'r'):
				if(item[1]):
					cpupoints = cpupoints + 1
			elif(randomItem == 'Scissors' and userinput == 'r'):
				if(item[2]):
					userpoints = userpoints + 1
			elif(randomItem == 'Scissors' and userinput == 'p'):
				if(item[2]):
					cpupoints = cpupoints + 1

			print("CPU choice: ", randomItem)
			print("CPU: ",cpupoints)
			print("User points: ",userpoints)

		else:
			print("You didn't enter the right character")
			break

