first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))
operation = input("Enter the operation you want to perform: ")

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    print(first_num / second_num)
else:
    print("Invalid operation")