try:
    num_str = input("Enter a number: ")
    num = int(num_str)

    result = 10 / num
except ValueError:
    print("Invalid input, you didn't enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Exception handling complete.")