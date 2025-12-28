# First draft, needs refactoring to include edge cases. 
def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to the Car Loan Calculatron 9000!')

while True:
    prompt('Enter the loan amount')
    loan_amount = input()

    while invalid_number(loan_amount):
        prompt('Please enter a valid number!')
        loan_amount = input()

    prompt('Enter the Annual Percentage Rate (APR)')
    loan_apr = input()

    while invalid_number(loan_apr):
        prompt('Please enter a valid number!')
        loan_apr = input()

    prompt('Enter the loan duration (months)')
    loan_duration = input()

    while invalid_number(loan_duration):
        prompt('Please enter a valid number!')
        loan_duration = input()

    interest_rate = (float(loan_apr) / 100) / 12

    monthly_payment = round(float(loan_amount) * (interest_rate / (1 - ( 1 + interest_rate) ** (- float(loan_duration)))), 2)

    prompt(f'Your monthly payment is ${monthly_payment}')
    prompt('Would you like to perform another calculation? (y/n) ')
    answer = input()
    if answer and answer.lower() != 'y':
        break