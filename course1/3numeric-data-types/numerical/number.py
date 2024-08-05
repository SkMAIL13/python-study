num = int(input())

a = num // 100
b = (num // 10) % 10
c = num % 10

mid = a + b + c - max(a, b, c) - min(a, b, c)

if max(a, b, c) - min(a, b, c) == mid:
    print("Число интересное")
else:
    print("Число неинтересное")
