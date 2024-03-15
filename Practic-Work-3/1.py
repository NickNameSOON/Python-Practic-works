def power_numbers():
    nums = [float(input("Введіть число {}: ".format(i))) for i in range(1, 4)]
    for num in nums:
        if num >= 0:
            print("Квадрат числа {}: {}".format(num, num ** 2))
        else:
            print("Четверта ступінь числа {}: {}".format(num, num ** 4))

power_numbers()
