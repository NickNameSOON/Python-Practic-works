def main():
    color_number = int(input("Введіть номер кольору в веселці: "))

    warm_colors = [1, 2, 3,]
    cold_colors = [4, 5, 6, 7]

    if color_number in warm_colors:
        print("Цей колір відноситься до теплих кольорів.")
    elif color_number in cold_colors:
        print("Цей колір відноситься до холодних кольорів.")
    else:
        print("Введений номер коліру не відповідає жодному кольору в веселці.")


if __name__ == "__main__":
    main()

