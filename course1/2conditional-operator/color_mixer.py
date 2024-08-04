first_colour = str(input())
second_colour = str(input())

if (
    first_colour == "красный"
    and second_colour == "синий"
    or first_colour == "синий"
    and second_colour == "красный"
):
    print("фиолетовый")
elif (
    first_colour == "желтый"
    and second_colour == "синий"
    or first_colour == "синий"
    and second_colour == "желтый"
):
    print("зеленый")
elif (
    first_colour == "красный"
    and second_colour == "желтый"
    or first_colour == "желтый"
    and second_colour == "красный"
):
    print("оранжевый")
elif first_colour == "красный" and second_colour == "красный":
    print("красный")
elif first_colour == "желтый" and second_colour == "желтый":
    print("желтый")
elif first_colour == "синий" and second_colour == "синий":
    print("синий")
else:
    print("ошибка цвета")
