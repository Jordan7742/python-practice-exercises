"""Simple Calculator — adds, subtracts or multiplies two user-entered values."""

a = float(input("Input the first value: "))
b = float(input("Input the second value: "))
operation = input("A: Add, S: Subtract, M: Multiply: ").upper()

if operation == "A":
    print("Result:", a + b)
elif operation == "S":
    print("Result:", a - b)
elif operation == "M":
    print("Result:", a * b)
else:
    print("Please enter A, S or M.")
