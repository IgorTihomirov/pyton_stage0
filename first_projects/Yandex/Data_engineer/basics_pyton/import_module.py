# Из модуля math импортируйте функцию, вычисляющую факториал числа
# и задайте ей псевдоним fact.
from math import factorial as fact
# Из модуля random импортируйте функцию, возвращающую случайное число
# и задайте ей псевдоним rnd.
from random import randint as rnd

# С помощью функции под псевдонимом rnd присвойте переменной value
# случайное значение в диапазоне от 1 до 10 включительно.
value = rnd(1, 10)

# С помощью функции под псевдонимом fact вычислите факториал числа,
# сохранённого в переменной value.
result = fact(value)

# Распечатайте результат в нужном формате.
# Для печати нескольких значений перечислите их через запятую.
print('Факториал', value, 'равен', result)