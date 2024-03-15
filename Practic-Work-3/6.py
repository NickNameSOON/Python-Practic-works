def replace_integers():
    a = int(input("Введіть перше ціле число a: "))
    b = int(input("Введіть друге ціле число b: "))

    if a != b:
        max_num = max(a, b)
        print("Нове значення обох чисел: {}".format(max_num))
    else:
        print("Числа рівні, замінюємо їх нулями.")
        print("Нове значення обох чисел: 0")


replace_integers()
