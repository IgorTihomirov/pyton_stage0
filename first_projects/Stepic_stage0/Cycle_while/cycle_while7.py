number = int(input())
total = 0
while number > 0 and number < 6:
    if number == 5:
        total += 1
    number = int(input())
print(total)