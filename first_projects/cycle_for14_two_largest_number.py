n = int(input())
largest = 0
largest1 = 0
for _ in range(n):
    num = int(input())
    if num > largest:
        largest1 = largest
        largest = num
    elif largest1 < num < largest:
        largest1 = num
print(largest, largest1, sep='\n')