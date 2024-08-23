word = input()
count = 0

while not (word == "стоп" or word == "хватит" or word == "достаточно"):
    count += 1
    word = input()
print(count)
