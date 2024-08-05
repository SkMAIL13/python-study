num = int(input())

first = num // 100
second = (num // 10) % 10
last = num % 10

mid = first + second + last - max(first, second, last) - min(first, second, last)

if max(first, second, last) - min(first, second, last) == mid:
    print("Число интересное")
else:
    print("Число неинтересное")
