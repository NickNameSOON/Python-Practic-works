var1 = 10
var2 = -5

logical_expr_and_1 = (var1 > 0) and (var2 > 0)  # True and False = False
logical_expr_and_2 = (var1 > 0) and (var2 < 0)  # True and True = True
logical_expr_and_3 = (var1 < 0) and (var2 > 0)  # False and False = False
logical_expr_and_4 = (var1 < 0) and (var2 < 0)  # False and True = False

logical_expr_or_1 = (var1 > 0) or (var2 > 0)  # True or False = True
logical_expr_or_2 = (var1 > 0) or (var2 < 0)  # True or True = True
logical_expr_or_3 = (var1 < 0) or (var2 > 0)  # False or False = False
logical_expr_or_4 = (var1 < 0) or (var2 < 0)  # False or True = True

str_var1 = "Hello"
str_var2 = "World"
str_logical_expr_or = (str_var1 == "Hello") or (str_var2 == "World")

if var1 > 0:
    print("Значення змінної більше 0.")
elif var1 < 0:
    print("Значення змінної менше 0.")

if var1 > 0:
    print(1)
else:
    print(-1)

third_var = None
if var1 > var2:
    third_var = var1 - var2
elif var1 < var2:
    third_var = var1 + var2
else:
    third_var = var1
print(third_var)

