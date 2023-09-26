# Data types in python
# In python everything is an object

# Buildin data types
# 1. Numbers: Integers, Floats, Complex
# 2. Strings: Sequence of characters
# 3. Boolean: True or False
# 4. Sequence: List, Tuple, Range
# 5. Mapping: Dictionary

# 1. Numbers---------------->
# Integers, Floats and Complex
a = 10
b = 10.5
c = complex(10, 5)
print(type(a)) #------> <class 'int'>
print(type(b)) #------> <class 'float'>
print(type(c)) #------> <class 'complex'>

# 2. Strings---------------->
# Sequence of characters
d = "Hello World"
print(type(d)) #------> <class 'str'>

# 3. Boolean---------------->
# True or False
e = True
print(type(e)) #------> <class 'bool'>

# 4. Sequence---------------->
# List, Tuple, Range
list = [1, 2, 3, 4, 5, ['apple', 'banana', 'orange']] #List is mutable
tuple = (1, 2, 3, 4, 5, ('apple', 'banana', 'orange')) #Tuple is immutable
range = range(1, 10) #Range is immutable

print(type(list)) #------> <class 'list'>
print(type(tuple)) #------> <class 'tuple'>
print(type(range)) #------> <class 'range'>

# 5. Mapping---------------->
# Dictionary
dict = {'name': 'John', 'age': 30, 'address': 'USA'} #Dictionary is mutable, it's key value pair like object in javascript
print(type(dict)) #------> <class 'dict'>

