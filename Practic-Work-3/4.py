def replace_numbers():
    x = float(input("Введіть перше число x: "))
    y = float(input("Введіть друге число y: "))

    if x != y:
        smaller = min(x, y)
        bigger = max(x, y)

        new_smaller = (x + y) / 2
        new_bigger = bigger * 2

        print("Нове значення меншого числа: {}".format(new_smaller))
        print("Нове значення більшого числа: {}".format(new_bigger))
    else:
        print("Числа рівні, замінюємо їх нулями.")
        print("Нове значення обох чисел: 0")


replace_numbers()
