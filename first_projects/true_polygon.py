from math import tan, pow, pi
n = float(input())
a = float(input())
s = (n * pow(a, 2)) / (4 * tan(pi / n))
print(s)
