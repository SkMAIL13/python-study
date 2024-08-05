a, b, c = int(input()), int(input()), int(input())

print(max(a, b, c))

if a <= b <= c or c <= b <= a:
    print(b)
elif a <= c <= b or b <= c <= a:
    print(c)
elif b <= a <= c or c <= a <= b:
    print(a)

print(min(a, b, c))
