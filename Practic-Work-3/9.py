def count_integers():
    a = float(input("Введіть перше число a: "))
    b = float(input("Введіть друге число b: "))
    c = float(input("Введіть третє число c: "))

    count = sum(num.is_integer() for num in [a, b, c])
    print("Кількість цілих чисел: {}".format(count))


count_integers()
