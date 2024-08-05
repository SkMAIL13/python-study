num = int(input())

if num % 2 != 0:
    print("YES")
elif num % 2 == 0:
    if 2 <= num <= 5:
        print("NO")
    elif 6 <= num <= 20:
        print("YES")
    elif num > 20:
        print("NO")