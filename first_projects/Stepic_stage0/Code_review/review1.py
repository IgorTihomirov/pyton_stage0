# задача - https://stepik.org/lesson/311433/step/3?unit=293861
count = 0
p = 1 # здесь была ошибка -> p = 0, при таком раскладе произведение числе всегда было бы = 0
for i in range(1, 11): # здесь была ошибка в границах, не включена права граница (1,10)
    x = int(input())
    if x >= 0: # здесь было неравенство x > 0, но 0 это тоже неотрицательное число
        p = p * x
        count = count + 1
if count > 0:
    print(count) # здесь была ошибка. Выводилось print(x), а нужно было count
    print(p)
else:
    print('NO')