x = 4.0
y = 0.2
a = 1.0
c = 2.0
d = 3.0

if x > 3 and x * y < 2:
    z = max(3 ** (x + a), c + d, min(x, a))
elif x > 3 and x * y > 2:
    z = min(x, a, c, y, d)
else:
    z = 3 * c + d * x

print("x = " + str(x) + ", " + "y = " + str(y) + ", " + "a = " + str(a) + ", " + "c = " + str(c) + ", " + "d = " + str(d))
if z is None:
    print("Формула для этих данных не задана.")
else:
    print("Результат = " + str(z))
