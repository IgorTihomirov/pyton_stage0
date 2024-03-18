from math import sqrt, pow
a = float(input())
b = float(input())
a1 = (a+b) / 2
a2 = sqrt(a * b)
a3 = 2 * a * b / (a + b)
a4 = sqrt((pow(a, 2) + pow(b, 2))/ 2)
print(a1)
print(a2)
print(a3)
print(a4)
