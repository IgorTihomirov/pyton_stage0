even = 0
for _ in range(1, 11):
    num = int(input())
    if num % 2 == 0:
        even += 1
if even == 10:
    print('YES')
else:
    print('NO')