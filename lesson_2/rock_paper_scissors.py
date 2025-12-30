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

def game_outcome(player, npc):
    global player_count
    global computer_count

    if npc in RULE_DICT[player]:
        player_count += 1
        prompt('You win!')
    elif player in RULE_DICT[npc]:
        computer_count += 1
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

player_count = 0
computer_count = 0

prompt(MESSAGES['rules'])

while True:
    prompt(f"Choose one: {', '.join(LABEL_DICT.values())}")
    prompt(MESSAGES['instruction'])
    player_choice = input().casefold()

    while player_choice not in LABEL_DICT:
        prompt('Please enter a valid choice!')
        player_choice = input().casefold()

    computer_choice = random.choice(list(LABEL_DICT.values()))

    prompt(
        f'You chose {LABEL_DICT[player_choice]}, '
        f'the computer chose {computer_choice}!'
    )

    for key, value in LABEL_DICT.items():
        if value == computer_choice:
            computer_choice = key
            break

    game_outcome(player_choice, computer_choice)

    print(f'Player wins: {player_count}, Computer wins: {computer_count}')

    if player_count == 3 or computer_count == 3:
        break

    prompt(MESSAGES['again'])
    play_again = input().casefold()

    while True:
        if play_again.startswith('n') or play_again.startswith('y'):
            break

        prompt(MESSAGES['again_validate'])
        play_again = input().casefold()

    if play_again[0] == 'n':
        break