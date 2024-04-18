# задача https://stepik.org/lesson/311433/step/8?unit=293861
n = int(input()) # здесь была ошибка n = input(), в такое записи n это строка, а не число
product = 1 # здесь была ошибка product = n % 10. Это исказит общее произведение цифр числа
while n > 0: # while n >= 10: Нам нужно дойти до конца числа
    digit = n % 10
    product = product * digit
    n //= 10
print(product)