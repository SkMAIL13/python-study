a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print("Равносторонний")
elif a == b or b == c or a == c:
    print("Равнобедренный")
elif a != b and b != c and a != c:
    print("Разносторонний")
