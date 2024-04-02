flag = True
for _ in range(10):
    num = int(input())
    if num % 2 == 1:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO')