number = int(input())
max_num = 0
min_num = 9

while number > 0:
    last_digit = number % 10

    if max_num <= last_digit:
        max_num = last_digit
    if min_num >= last_digit:
        min_num = last_digit

    number = number // 10

print("Максимальная цифра равна", max_num)
print("Минимальная цифра равна", min_num)
