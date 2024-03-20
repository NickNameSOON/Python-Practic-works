def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Ряд чисел Фібоначчі від 1 до 20:")
for i in range(1, 21):
    print(fibonacci(i), end=" ")

print("Ряд парних чисел від 0 до 20:")
for i in range(0, 21, 2):
    print(i, end=" ")

print("\n")

print("Кожне третє число в ряді від -1 до -21:")
for i in range(-1, -22, -3):
    print(i, end=" ")


