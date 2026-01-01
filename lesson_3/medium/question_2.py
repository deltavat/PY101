#   Alan wrote the following function, which was intended to return all of the factors of number:
#       
#   Copy Code
#   def factors(number):
#       divisor = number
#       result = []
#       while divisor != 0:
#           if number % divisor == 0:
#               result.append(number // divisor)
#           divisor -= 1
#       return result
#   Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we're not looking to find the factors for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.
#   
#   Bonus Question: What is the purpose of number % divisor == 0 in that code?

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(-10))

# number % divisor == 0 is for evaluating a remainder of 0