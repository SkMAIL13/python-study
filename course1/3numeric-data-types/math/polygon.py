import math

n = int(input())
a = float(input())

square = (n * pow(a, 2)) / (4 * math.tan(math.pi / n))

print(float(square))
