num, num2, num3 = int(input()), int(input()), int(input())

if num < num2 < num3 or num3 < num2 < num:
    print(num2)
elif num2 < num < num3 or num3 < num < num2:
    print(num)
elif num < num3 < num2 or num2 < num3 < num:
    print(num3)
