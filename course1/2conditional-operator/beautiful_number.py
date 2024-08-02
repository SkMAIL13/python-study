num = int(input())

if (num % 7 == 0 or num % 17 == 0) and (999 < num <= 9999):
    print("YES")
else:
    print("NO")
