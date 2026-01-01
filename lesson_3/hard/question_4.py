#   Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.
#   
#   Alyssa supplied Ben with a function named is_an_ip_number. It determines whether a string is a numeric string between 0 and 255 as required for IP numbers and asked Ben to use it. Here's the code that Ben wrote:
#   
#   Copy Code
#   def is_dot_separated_ip_address(input_string):
#       dot_separated_words = input_string.split(".")
#       while len(dot_separated_words) > 0:
#           word = dot_separated_words.pop()
#           if not is_an_ip_number(word):
#               break
#           
#       return True
#   Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. You're not returning a false condition, and you're not handling the case when the input string has more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."
#   
#   Help Ben fix his code.


#   Here's Alyssa's is_an_ip_number function so you can test your code:

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

#   Old solution before learning about more pythonic guardrails and prioritise a short circuit.

#   def is_dot_separated_ip_address(input_string):
#       dot_separated_words = input_string.split(".")
#       if len(dot_separated_words) == 4:
#           while len(dot_separated_words) > 0:
#               word = dot_separated_words.pop()
#               if not is_an_ip_number(word):
#                   return False
#               
#           return True
#       return 'Invalid'


def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
            
    return True


print(is_dot_separated_ip_address('192.168.0.11')) # True
print(is_dot_separated_ip_address('192.168.0')) # False
print(is_dot_separated_ip_address('192.168.0.1234')) # False
print(is_dot_separated_ip_address('192.lol.0.1234')) # False