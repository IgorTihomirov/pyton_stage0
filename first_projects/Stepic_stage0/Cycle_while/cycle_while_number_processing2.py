num = int(input())
total = str()
while num != 0:
    last_digit = num % 10
    last_digit1 = str(last_digit)
    total += last_digit1
    num = num // 10
print(total)