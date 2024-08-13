m, n = int(input()), int(input())

for i in range(m % 2 - 1 + m, n, -2):
    print(i)
