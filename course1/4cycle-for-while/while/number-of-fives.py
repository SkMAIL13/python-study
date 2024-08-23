grade = int(input())
count = 0

while 0 < grade <= 5:
    if grade == 5:
        count += 1

    grade = int(input())

print(count)
