def common_divisor():
    a = float(input("Введіть перше число a: "))
    b = float(input("Введіть друге число b: "))
    c = float(input("Введіть третє число c: "))
    k = float(input("Введіть число k: "))

    divisors = [num for num in [a, b, c] if num % k == 0]

    if divisors:
        print("Число {} є дільником чисел: {}".format(k, divisors))
    else:
        print("Число {} не є дільником жодного з введених чисел.".format(k))


common_divisor()
