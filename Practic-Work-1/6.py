def calculate_y(a, b, n, x, m):
  
  # Обчислення (a + b)^n
  power_ab = (a + b) ** n

  # Обчислення x^m
  power_x = x ** m

  # Обчислення b^(n - n)
  power_b = b ** (n - n)

  # Обчислення знаменника
  denominator = 1 + x / (power_x + power_b)

  # Обчислення Y
  y = power_ab / denominator

  return y

a = 2
b = 3
n = 4
x = 5
m = 2


y = calculate_y(a, b, n, x, m)

print(f"Y = {y}")
