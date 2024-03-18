from math import sin, cos, tan, radians
x = float(input())
x = radians(x)
a = sin(x) + cos(x) + pow(tan(x), 2)
print(a)
