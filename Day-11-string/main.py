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


# String Slicing & Operations on String------------------------>
# Length of a String
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

pie = "ApplePie"
print(pie[:5]) #Returns characters from beginning to 5th index (not included)
print(pie[6])	#returns the 6th index
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

print(fruit[-1: - 3]) #It means print(fruit[len(fruit) -1:len(fruit) - 3]), returns 4th to 2nd(not included) index, here returns nothing cause 4th to 2nd index is not possible
print(fruit[-3:-1]) #returns 2nd to 4th()not included index, here returns 'ng'

'''
So the fact is while slicing the first index is included and the last index is not included. So after : the index position will be given index - 1.
'''