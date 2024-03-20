def calculate_y(a, b, n, x, m):
  power_ab = (a + b) ** n
  power_x = x ** m
  power_b = b ** (n - n)
  denominator = 1 + x / (power_x + power_b)
  y = power_ab / denominator
  return y

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
n = int(input("Enter a number n: "))
x = int(input("Enter a number x: "))
m = int(input("Enter a number m: "))


y = calculate_y(a, b, n, x, m)

print(f"Y = {y}")
