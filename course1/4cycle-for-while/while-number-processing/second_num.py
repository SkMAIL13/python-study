number = int(input())
second_number = 0

while number > 10:
    second_number = number % 10

    number //= 10
print(second_number)
