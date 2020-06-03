#!/usr/bin/python

input1 = 0.0
input2 = 0.0
operator = " "

while operator:
	try:
	 	input1 = float(input("Enter first number: "))
	except ValueError:
	 	print("You didn't enter an integer")
	 	break
	try:
	 	operator = str(input("Enter operator: "))
	except ValueError:
	 	print("How did you fuck this up!")
	 	break
	try:
		input2 = float(input("Enter second number: "))
	except ValueError:
		print("You didn't enter an integer")
		break

	if operator == '*':
	 	sum = input1 * input2
	 	print(sum)
	elif operator == '+':
	 	sum = input1 + input2
	 	print(sum)
	elif operator == '/':
	 	sum = input1 / input2
	 	print(sum)
	elif operator == '-':
		sum = input1 - input2
		print(sum)
	else:
	 	print("You did not enter an operator")
