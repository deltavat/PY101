# Given the following similar sets of code, what will each code snippet print?


# A
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one
    
one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

#   one is: ['one']
#   two is: ['two']
#   three is: ['three']


# B

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]
    
one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

#   one is: ['one']
#   two is: ['two']
#   three is: ['three']


# C

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"
    
one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

#   one is: ['two']
#   two is: ['three']
#   three is: ['one']

# modifying through a function only works for C, as local/global rules don't apply to mutating lists.