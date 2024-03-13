import math


def distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def closer_point():
    x1, y1 = map(float, input("Введіть координати точки A (x1 y1): ").split())
    x2, y2 = map(float, input("Введіть координати точки B (x2 y2): ").split())

    dist1 = distance(x1, y1)
    dist2 = distance(x2, y2)

    if dist1 < dist2:
        print("Точка A знаходиться ближче до початку координат.")
    elif dist1 > dist2:
        print("Точка B знаходиться ближче до початку координат.")
    else:
        print("Точки розташовані на однаковій відстані до початку координат.")


closer_point()
