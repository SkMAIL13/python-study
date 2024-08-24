number = int(input())

summ = 0
count = 0
multiply = 1
average = 0
first_digit = 0
last_digit = number % 10

while number != 0:
    first = number % 10
    summ += first
    count += 1
    multiply *= first

    number //= 10
print(summ, count, multiply, summ / count, first, first + last_digit, sep="\n")
