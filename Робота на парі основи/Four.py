def calculate_expression(n):
    nn = int(str(n) + str(n))
    nnn = int(str(n) + str(n) + str(n))
    result = n + nn + nnn
    return result

n = 5

result = calculate_expression(n)
print(f"Результат виразу {n} + {n}{n} + {n}{n}{n} дорівнює: {result}")
