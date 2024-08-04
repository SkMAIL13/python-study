x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

x = x1 - x2
y = y1 - y2

if -1 <= x <= 1 and -1 <= y <= 1:
    print("YES")
else:
    print("NO")
