a, b = int(input()), int(input())

counter = 0
for i in range(a, b + 1):
    if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
        counter = counter + 1
    elif (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
        counter = counter + 1
print(counter)
