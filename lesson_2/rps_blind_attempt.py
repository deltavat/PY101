import random

def prompt(message):
    print(f"==> {message}")

def computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

prompt('Welcome to Rock Paper Scissors!')

while True:
    prompt('Enter Rock, Paper, or Scissors:')
    player_choice = input().title()

    while player_choice not in ['Rock', 'Paper', 'Scissors']:
        prompt('Please enter a valid choice! Rock, Paper, or Scissors:')
        player_choice = input().title()
    
    computer = computer_choice()
    
    if computer == 'Rock' and player_choice == 'Scissors':
        prompt(f'Computer chose {computer}, Computer wins!')
    elif computer == 'Paper' and player_choice == 'Rock':
        prompt(f'Computer chose {computer}, Computer wins!')
    elif computer == 'Scissors' and player_choice == 'Paper':
        prompt(f'Computer chose {computer}, Computer wins!')
    elif computer == 'Scissors' and player_choice == 'Rock':
        prompt(f'Computer chose {computer}, You win!')
    elif computer == 'Rock' and player_choice == 'Paper':
        prompt(f'Computer chose {computer}, You win!')
    elif computer == 'Paper' and player_choice == 'Scissors':
        prompt(f'Computer chose {computer}, You win!')
    else:
        prompt(f'Computer chose {computer}, It\'s a tie!')
    
    prompt('Play again? (y/n) ')
    answer = input()
    if answer and answer.lower() != 'y':
        break