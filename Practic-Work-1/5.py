def point_location():
    x, y = map(float, input("Введіть координати точки A (x y): ").split())

    if x == 0 and y == 0:
        print("Точка розташована у початку координат.")
    elif x == 0:
        print("Точка розташована на осі Y.")
    elif y == 0:
        print("Точка розташована на осі X.")
    elif x > 0 and y > 0:
        print("Точка розташована у першому квадранті.")
    elif x < 0 and y > 0:
        print("Точка розташована у другому квадранті.")
    elif x < 0 and y < 0:
        print("Точка розташована у третьому квадранті.")
    else:
        print("Точка розташована у четвертому квадранті.")


point_location()