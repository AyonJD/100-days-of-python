'''
Typecasting in python------>
The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.
-----------------------------------------------------

Two Types of Typecasting:-
1. Implicit Typecasting
2. Explicit Typecasting

1. Implicit Typecasting:-
--------------------------
Implicit typecasting is the automatic conversion of one data type into another data type by the python interpreter.

Example:-
a = 10
b = 20.5
c = a + b
print(c)
print(type(c))

Output:-
<class 'int'>
<class 'float'>
30.5
<class 'float'>

2. Explicit Typecasting:-
--------------------------
Explicit typecasting is the conversion of one data type into another data type by the user.

Example:-
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

Output:-
The Sum of both the numbers is 22

'''