import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
	print(f'==> {message}')

def rpc_mechanic(player, npc):
	if ((player == 'rock' and npc == 'scissors') or
		(player == 'paper' and npc == 'rock') or
		(player == 'scissors' and npc == 'paper')):
		prompt('You win!')
	elif ((player == 'scissors' and npc == 'rock') or
		(player == 'rock' and npc == 'paper') or
		(player == 'paper' and npc == 'scissors')):
		prompt('Computer wins!')
	else:
		prompt("It's a tie!")

game = True

while game:
	prompt(f'Welcome, Player! Choose one: {', '.join(VALID_CHOICES)}')
	choice = input()
	
	while choice not in VALID_CHOICES:
		prompt('Please enter a valid choice!')
		choice = input()
	
	computer_choice = random.choice(VALID_CHOICES)
	
	prompt(f'You chose {choice}, the computer chose {computer_choice}!')
	
	rpc_mechanic(choice, computer_choice)

	prompt('Play again? (y/n)')
	again = input().lower()
	while True:
		if again.startswith('n') or again.startswith('y'):
			break
		
		prompt('Please enter "y" or "n": ')
		again = input().lower()
	
	if again[0] == 'n':
		game = False