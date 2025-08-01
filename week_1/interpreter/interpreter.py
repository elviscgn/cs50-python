num1, operator, num2 = input("Expression: ").split()

if operator == "+":
    result = float(num1) + float(num2)
elif operator == "-":
    result = float(num1) - float(num2)
elif operator == "*":
    result = float(num1) * float(num2)
elif operator == "/":
    result = float(num1) / float(num2)

print(result)