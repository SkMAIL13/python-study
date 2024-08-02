num = int(input())

first_digit = num // 1000
second_digit = (num // 100) % 10
third_digit = (num // 10) % 10
last_digit = num % 10

print("Цифра в позиции тысяч равна", first_digit)
print("Цифра в позиции сотен равна", second_digit)
print("Цифра в позиции десятков равна", third_digit)
print("Цифра в позиции единиц равна", last_digit)