from math import sin, cos, tan, pow, radians

x = float(input())

radian = radians(x)

res = sin(radian) + cos(radian) + pow(tan(radian), 2)

print(res)
