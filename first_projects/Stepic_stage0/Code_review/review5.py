# задача https://stepik.org/lesson/311433/step/7?unit=293861
n = int(input())
while n > 0:
    first_digit = n % 10 # добавлена переменная first_digit
    n //= 10 # этой строчки не было. Так мы "урочиваем" число до последней цифры
print(first_digit) # здесь была ошибка print(n). Выводим переменную, которую мы перезаписываем
