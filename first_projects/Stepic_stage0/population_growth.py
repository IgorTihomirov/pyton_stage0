m = float(input())
p = float(input())
n = int(input())
for i in range(n):
    print(i+1, m)
    m = m * (1 + p / 100)
