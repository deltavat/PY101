# Ask the user for the first number.
# Ask the user for the second number. 
# Ask the user for an operation to perform. 
# Perform the operation on the two numbers.
# Print the result to the terminal.

print('Welcome to Calculatron 9000!')

# Ask the user for the first number
print("What's the first number?")
number1 = input()
print("What's the second number?")
number2 = input()

while True: # added while loop to cover invalid operation option
	print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
	operation = input()

	if operation =='1': 							# addition
		output = int(number1) + int(number2)
		break										# exit loop
	elif operation == '2':							# subtract
		output = int(number1) - int(number2)
		break
	elif operation == '3':							# multiply
		output = int(number1) * int(number2)
		break
	elif operation == '4':							# divide
		output = int(number1) / int(number2)
		break
	else:
		print('Please enter a valid choice!')

print(f'The result is: {output}')