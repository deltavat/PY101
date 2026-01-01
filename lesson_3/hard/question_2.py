# What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# Try to answer without running the code or looking at the solution.

# [1, 2]
# {'first': [1, 2]} as original dictionary list object is mutated