def count_negative():
    a = float(input("Введіть перше число a: "))
    b = float(input("Введіть друге число b: "))
    c = float(input("Введіть третє число c: "))

    count = sum(num < 0 for num in [a, b, c])
    print("Кількість негативних чисел: {}".format(count))


count_negative()
