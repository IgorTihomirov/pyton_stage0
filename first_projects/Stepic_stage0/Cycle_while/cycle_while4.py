text = input()
total = 0
while not(text == 'стоп' or text == 'хватит' or text == 'достаточно'):
    total += 1
    text = input()
print(total)