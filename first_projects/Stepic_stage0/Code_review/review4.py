# задача https://stepik.org/lesson/311433/step/6?unit=293861
n = int(input())
max_digit = -1 # здесь была ошибка n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit: # здесь была ошибка if digit < max_digit: . Последня цифра должна быть больше, чтобы ее перезаписть в max_digit
            max_digit = digit # здесь была ошибка digit = max_digit. Нам нужно перезаписывать max_digit.
    n = n // 10 # здесь была ошибка n % 10. При каждом цикле мы должны отмечать последнюю цифру числа, чтобы проверить все цифры
if max_digit == -1: # здесь была ошибка if max_digit == 0:. Если max_digit останется - 1, значит за все итерации так и не нашлось цифры кратной 3
    print('NO')
else:
    print(max_digit)