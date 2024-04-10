num = int(input())
last_digit1 = num % 10
flag = True
while num != 0:
    last_digit = num % 10
    if last_digit1 > last_digit:
        flag = False
    last_digit1 = last_digit
    num = num // 10
if flag == True:
    print('YES')
else:
    print('NO')
