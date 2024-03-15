def triangle_angles():
    angle1 = float(input("Введіть перший кут трикутника: "))
    angle2 = float(input("Введіть другий кут трикутника: "))
    angle_sum = 180

    if angle1 + angle2 < angle_sum and angle1 > 0 and angle2 > 0:
        angle3 = angle_sum - angle1 - angle2
        print("Такий трикутник існує.")
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("Трикутник є прямокутним.")
        else:
            print("Трикутник не є прямокутним.")
    else:
        print("Такий трикутник не існує або введено невірні значення кутів.")


triangle_angles()
