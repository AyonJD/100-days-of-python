# Multiline Strings-------------------->
# If our string has multiple lines, we can create them like this:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Accessing Characters of a String------>
'''
In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.
'''

name = "Ayon Jodder"
print(name[0])
print(name[1])
print('\n')

# Output:-
# A
# y

# Looping through the string-------------->
'''
We can loop through the string using for loop.
'''

for char in name:
    print(char)