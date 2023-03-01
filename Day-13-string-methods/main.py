# String methods------------------------------->
'''
Python provides a set of built-in methods that we can use to alter and modify the strings.
'''

# 1. upper() : Converts a string into upper case
# Example:-
str1 = "AbcDEfghIJ"
print(str1.upper()) #Output: ABCDEFGHIJ

# 2. lower() : Converts a string into lower case
# Example:-
str2 = "AbcDEfghIJ"
print(str2.lower()) #Output: abcdefghij

# 3. strip() : Removes any whitespace from the beginning or the end
# Example:-
str3 = "   Hello World   "
print(str3.strip()) #Output: Hello World

# 4. rstrip() : Removes any trailing characters
# Example:-
str4 = "Hello World   "
print(str4.rstrip()) #Output: Hello World
str4 = "Hello !!!"
print(str4.rstrip("!")) #Output: Hello

# 5. replace() : Replaces a string with another string
# Example:-
str5 = "Hello World"
print(str5.replace("H", "J")) #Output: Jello World

# 6. split() : Splits the string into substrings if it finds instances of the separator
# Example:-
str6 = "Hello World"
print(str6.split(' ')) #Output: ['Hello', 'World']

# 7. capitalize() : Converts the first character to upper case
# Example:-
str7 = "hello world"
print(str7.capitalize()) #Output: Hello world

# 8. center() : Returns a centered string
# Example:-
str8 = "Hello World"
print(str8.center(100)) #Output:    Hello World
# We can also provide padding character. It will fill the rest of the fill characters provided by the user.
print(str8.center(100, ".")) #Output: ..................Hello World..................

# 9. count() : Returns the number of times a specified value occurs in a string
# Example:-
str9 = "Hello World"
print(str9.count("l")) #Output: 3

# 10. endswith() : Returns true if the string ends with the specified value
# Example:-
str10 = "Hello World"
print(str10.endswith("d")) #Output: True
# We can even also check for a value in-between the string by providing start and end index positions.
print(str10.endswith("o", 0, 5)) #Output: True.....It means check if the string ends with 'o' from 0th index to 5th index(not included)

# 11. find() : Searches the string for a specified value and returns the position of where it was found
# Example:-
str11 = "He's name is Dan. He is an honest man."
print(str11.find("is")) #Output: 10
# If the value is not found, the find() method returns -1

# 12. index() : Searches the string for a specified value and returns the position of where it was found
# Example:-
str12 = "He's name is Dan. Dan is an honest man."
print(str12.index("Dan")) #Output: 13
# If the value is not found, the index() method raises an exception (ValueError: substring not found)

# find() and index() are similar. The only difference is that the index() method raises an exception if the value is not found.

# 13. isalnum() : Returns True if all characters in the string are alphanumeric
# Example:-
str13 = "HelloWorld"
print(str13.isalnum()) #Output: True
str13 = "Hello World"
print(str13.isalnum()) #Output: False

# 14. isalpha() : Returns True if all characters in the string are in the alphabet
# Example:-
str14 = "HelloWorld"
print(str14.isalpha()) #Output: True
str14 = "Hello World"
print(str14.isalpha()) #Output: False

# 15. islower() : Returns True if all characters in the string are lower case
# Example:-
str15 = "HelloWorld"
print(str15.islower()) #Output: False
str15 = "helloworld"
print(str15.islower()) #Output: True

# 16. isupper() : Returns True if all characters in the string are upper case
# Example:-
str16 = "HelloWorld"
print(str16.isupper()) #Output: False
str16 = "HELLOWORLD"
print(str16.isupper()) #Output: True

# 17. isprintable() : Returns True if all characters in the string are printable
# Example:-
str17 = "HelloWorld"
print(str17.isprintable()) #Output: True
str17 = "\n"
print(str17.isprintable()) #Output: False

# 18. isspace() : Returns True if all characters in the string are whitespaces
# Example:-
str18 = "HelloWorld"
print(str18.isspace()) #Output: False
str18 = " "
print(str18.isspace()) #Output: True

# 19. istitle() : Returns True if the string follows the rules of a title
# Example:-
str19 = "World Health Organization"
print(str19.istitle()) #Output: True
str19 = "To kill a Mocking bird"
print(str19.istitle()) #Output: False

# 20. isupper() : Returns True if all characters in the string are upper case
# Example:-
str20 = "HelloWorld"
print(str20.isupper()) #Output: False
str20 = "HELLOWORLD"
print(str20.isupper()) #Output: True

# 21. join() : Joins the elements of an iterable to the end of the string
# Example:-
str21 = "Hello World"
print(" ".join(str21)) #Output: H e l l o   W o r l d
print("".join(str21)) #Output: HelloWorld

# 22. startswith() : Returns true if the string starts with the specified value
# Example:-
str22 = "Hello World"
print(str22.startswith("Hello")) #Output: True
# We can even also check for a value in-between the string by providing start and end index positions.
print(str22.startswith("o", 0, 5)) #Output: False.....It means check if the string starts with 'o' from 0th index to 5th index(not included)

# 23. swapcase() : Swaps cases, lower case becomes upper case and vice versa
# Example:-
str23 = "Hello World"
print(str23.swapcase()) #Output: hELLO wORLD

# 24. title() : Converts the first character of each word to upper case
# Example:-
str24 = "He's name is Dan. Dan is an honest man."
print(str24.title()) #Output: He'S Name Is Dan. Dan Is An Honest Man.
# ----------------->>>>
