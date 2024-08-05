a, b, c = str(input()), str(input()), str(input())

len1, len2, len3 = len(a), len(b), len(c)

min = min(len1, len2, len3)
max = max(len1, len2, len3)

if min == len1:
    print(a)
elif min == len2:
    print(b)
else:
    print(c)
if max == len1:
    print(a)
elif max == len2:
    print(b)
else:
    print(c)
