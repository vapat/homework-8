print("calculator")

x = int(input("enter your 1 number: "))
y = int(input("enter your 2 number: "))

operation = input("enter your operation: ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("error")