number = int(input())
last_digit = number % 10
count = 0

while number != 0:
    temp = number % 10
    if temp != last_digit:
        count += 1
    number //= 10
if count != 0:
    print("NO")
else:
    print("YES")
