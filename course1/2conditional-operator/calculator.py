a, b = int(input()), int(input())
symbol = str(input())

if symbol == "+":
    print(a + b)
elif symbol == "-":
    print(a - b)
elif symbol == "*":
    print(a * b)
elif symbol == "/":
    if b == 0:
        print("На ноль делить нельзя!")
    else:
        print(a / b)
else:
    print("Неверная операция")
