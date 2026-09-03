# Ask user for their name and age
name = input("What's your name: ")
age = input("What's your age: ")

# Say hello to the user and age
print("Hello", name)
print("Your age is:", age)

# Comment example
'''
Multiline comment
'''

# Print function parameters
# print(*objects, sep=' ', end='\n, file=sys.stdout, flush=False')

print("Hello", name, sep='\t')
print(f"Hello, {name}")