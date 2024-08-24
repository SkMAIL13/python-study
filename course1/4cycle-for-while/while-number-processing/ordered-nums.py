number = int(input())
last_digit = number % 10
flag = True

while number > 0:
    temp = number % 10

    if last_digit > temp:
        flag = False

    last_digit = number % 10
    number //= 10

if flag:
    print("YES")
else:
    print("NO")
