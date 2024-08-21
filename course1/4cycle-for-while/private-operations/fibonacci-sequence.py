n = int(input())
x = 1
y = 0

for _ in range(1, n + 1):
    x, y = y, x + y
    print(y, end=" ")
