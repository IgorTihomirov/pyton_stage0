# задача - https://stepik.org/lesson/311433/step/4?unit=293861
mx = -10**6 - 1 # здесь была ошибка, неверное указано начально значение перменной -> mx = 0. Из -за этого не работало условие на строке 8
s = 0
for i in range(10): # здесь была ошибка, неверно указан диапазон цикла -> range(11)
    x = int(input())
    if x < 0:
        s += x # здесь была ошибка -> s = x, а должна получиться сумма отрицательных чисел
        if x > mx: # здесь была ошибка. Условие x > mx должно быть вложено в условие x < 0
            mx = x
if s < 0:
    print(s)
    print(mx)
else:           # отсуствовало условие, при котором отрицательных чисел нет
    print('NO')
