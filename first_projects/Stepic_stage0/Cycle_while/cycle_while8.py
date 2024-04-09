coin = int(input())
total = 0
while coin >= 25:
    total += 1
    coin = coin - 25
while coin >= 10:
    total += 1
    coin = coin - 10
while coin >= 5:
    total += 1
    coin = coin - 5
while coin >= 1:
    total += 1
    coin = coin - 1
print(total)
