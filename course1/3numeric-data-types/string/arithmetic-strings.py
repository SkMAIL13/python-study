line1, line2, line3 = len(input()), len(input()), len(input())

max = max(line1, line2, line3)
min = min(line1, line2, line3)

ave = line1 + line2 + line3 - max - min

if max - ave == ave - min:
    print("YES")
else:
    print("NO")
