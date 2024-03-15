variable1 = 10
variable2 = -5


if variable1 > 0:
    print("Змінна variable1 більше 0")
else:
    print("Змінна variable1 менше або дорівнює 0")

if variable1 > 0:
    print(1)
else:
    print(-1)

third_variable = None

if variable1 > variable2:
    third_variable = variable1 - variable2
elif variable1 < variable2:
    third_variable = variable1 + variable2
else:
    third_variable = variable1

print("Значення третьої змінної:", third_variable)
