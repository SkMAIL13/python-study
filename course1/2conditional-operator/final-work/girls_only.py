age = int(input())
gender = str(input())

if 10 <= age <= 15:
    if gender == "f":
        print("YES")
    else:
        print("NO")
else:
    print("NO")
