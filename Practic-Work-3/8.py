def count_positive():
    a = float(input("Введіть перше число a: "))
    b = float(input("Введіть друге число b: "))
    c = float(input("Введіть третє число c: "))

    count = sum(num > 0 for num in [a, b, c])
    print("Кількість додатніх чисел: {}".format(count))


count_positive()
