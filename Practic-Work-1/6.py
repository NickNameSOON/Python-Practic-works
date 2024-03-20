def calculate_y(a, b, n, x, m):
  power_ab = (a + b) ** n
  power_x = x ** m
  power_b = b ** (n - n)
  denominator = 1 + x / (power_x + power_b)
  y = power_ab / denominator
  return y

a = float(input("Enter a number a: "))
b = float(input("Enter a number b: "))
n = float(input("Enter a number n: "))
x = float(input("Enter a number x: "))
m = float(input("Enter a number m: "))


y = calculate_y(a, b, n, x, m)

print(f"Y = {y}")
