s = 0 # здесь была ошибка s = 1. Сумма не должна начинаться с 1, иначе будет не корректный подсчет.
for i in range(7): # здесь была ошибка range (1, 7). Так как правая граница никогда не включается, циклов бы было 6, а не 7.
    n = int(input()) # здесь была ошибка n = input(), в такое записи n это строка, а не число
    if n % 2 == 0: # здесь была ошибка i % 2 == 0. Находили остаток от итераций цикла, а не от числа
        s += n
print(s)