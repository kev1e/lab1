import math
a = int(input())
b = int(input())
c = int(input())
d = b*b-4*a*c
if (d > 0):
    x1 = (-b + math.sqrt(d))/2*a
    x2 = (-b - math.sqrt(d))/2*a
    print(x1)
    print(x2)
if (d == 0):
    x = -b/2*a
    print(x)
else:
    print("NO RESULTS")