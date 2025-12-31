import random
import json

with open('rps.json', 'r') as file:
    MESSAGES = json.load(file)

RULE_DICT = {
    'r': ['l', 'sc'],
    'p': ['r', 'sp'],
    'sc': ['p', 'l'],
    'l': ['sp', 'p'],
    'sp': ['r', 'sc'],
}

LABEL_DICT = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock',
}

def prompt(message):
    print(f'==> {message}')

def determine_winner(player, npc):
    if npc in RULE_DICT[player]:
        prompt('You win!')
        return 'player'
    elif player in RULE_DICT[npc]:
        prompt('Computer wins!')
        return 'computer'
    else:
        prompt("It's a tie!")
        return 'tie'

def restart():
    prompt(MESSAGES['again'])
    play_again = input().casefold().strip()

    while not (play_again.startswith('n') or play_again.startswith('y')):
        prompt(MESSAGES['again_validate'])
        play_again = input().casefold().strip()
            
    return play_again[0] == 'y'

def get_player_choice():
    prompt(f"Choose one: {', '.join(LABEL_DICT.values())}")
    prompt(MESSAGES['instruction'])
    player_choice = input().casefold().strip()
    
    while player_choice not in LABEL_DICT:
        prompt('Please enter a valid choice!')
        player_choice = input().casefold().strip()
            
    return player_choice

def get_computer_choice():
    return random.choice(list(LABEL_DICT.keys()))

def display_choices(player, computer):
    prompt(
            f'You chose {LABEL_DICT[player]}, '
            f'the computer chose {LABEL_DICT[computer]}!'
        )

player_count = 0
computer_count = 0

prompt(MESSAGES['rules'])

while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    display_choices(player_choice, computer_choice)

    result = determine_winner(player_choice, computer_choice)
    
    if result == 'player':
        player_count += 1
    elif result == 'computer':
        computer_count += 1
    
    print(f'Player wins: {player_count}, Computer wins: {computer_count}')

    if player_count == 3 or computer_count == 3:
        prompt(MESSAGES['player_win'] if player_count == 3 else MESSAGES['computer_win'])

        if not restart():
            break

        player_count = 0
        computer_count = 0