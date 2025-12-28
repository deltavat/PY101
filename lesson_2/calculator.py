import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang='fr'):
    return MESSAGES[lang][message]

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt(messages('welcome'))

while True:
    prompt(messages('first'))
    number1 = input()

    while invalid_number(number1):
        prompt(messages('invalid_number'))
        number1 = input()

    prompt(messages('second'))
    number2 = input()

    while invalid_number(number2):
        prompt(messages('invalid_number'))
        number2 = input()

    prompt(messages('operation'))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages('operation_choice'))
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(f"The result is {output}")
    prompt(messages('repeat'))
    answer = input()
    if answer and answer.lower() != 'y':
        break