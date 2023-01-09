# Calculator

Num = input("please insert the firest number: ")
Num1 = input("please insert the second number: ")
operation = input("please insert your desird operation: + , - , * , /: ")
if operation == "+":
    result = float(Num) + float(Num1)
if operation == "-":
    result = float(Num) - float(Num1)
if operation == "*":
    result = float(Num) * float(Num1)
if operation == "/":
    result = float(Num) / float(Num1)

print(result)