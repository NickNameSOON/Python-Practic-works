def check_sequence(input_str):
    i = 0

    while i < len(input_str):
        # Знайти довжину послідовності нулів
        count_zeros = 0
        while i < len(input_str) and input_str[i] == '0':
            count_zeros += 1
            i += 1

        # Знайти довжину послідовності одиниць
        count_ones = 0
        while i < len(input_str) and input_str[i] == '1':
            count_ones += 1
            i += 1

        # Перевірити, чи довжина послідовності нулів і одиниць однакова
        if count_zeros != count_ones:
            return False

    # Якщо пройшли всі послідовності і вони відповідають умові
    return True

# Приклади використання:
sequence1 = "01010101"
result1 = check_sequence(sequence1)
print(f"Послідовність: {sequence1}, Результат: {result1}")

sequence2 = "00011100011"
result2 = check_sequence(sequence2)
print(f"Послідовність: {sequence2}, Результат: {result2}")
