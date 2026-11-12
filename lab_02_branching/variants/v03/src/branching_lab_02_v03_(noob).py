from math import exp, sin


x = 0.5
y = 2.0
a = 1.0

if x < 1 and y > 1:
    z = max(3 * sin(x), 2 * min(x, y), x + a)
elif x > 1 and y > 1:
    z = min((x + exp(x + a)) / 3, max(x, y))
else:
    z = 4 * sin(x * y)

print("x = " + str(x) + ", " + "y = " + str(y) + ", " + "a = " + str(a))
if z is None:
    print("Формула для этих данных не задана.")
else:
    print("Результат = " + str(z))
