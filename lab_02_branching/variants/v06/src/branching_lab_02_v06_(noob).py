from math import sin


x = 6.0
b = 0.5
c = 2.0

if c > 0 and x > 2:
    z = max(c, x / c, sin(c))
elif c < 0 and x > 2:
    z = min(c, c * x + sin(b), max(c, b))
else:
    z = max(c, b)

print("x = " + str(x) + ", b = " + str(b) + ", c = " + str(c))
print("Z = " + str(z))
