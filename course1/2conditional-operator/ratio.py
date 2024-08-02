num = int(input())

first_digit = num // 1000
second_digit = (num % 1000) // 100
third_digit = (num % 100) // 10
last_digit = num % 10

sum = first_digit + last_digit
dif = second_digit - third_digit

if sum == dif:
    print("ДА")
else:
    print("НЕТ")
