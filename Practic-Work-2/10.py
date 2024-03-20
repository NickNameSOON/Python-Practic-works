def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

count = 0

for num in range(100, 1000):
    divisor_sum = sum([i for i in range(1, num + 1) if num % i == 0 and is_prime(i)])
    if divisor_sum % 5 == 0:
        count += 1

print("Кількість тризначних чисел, сума простих дільників яких кратна 5:", count)

