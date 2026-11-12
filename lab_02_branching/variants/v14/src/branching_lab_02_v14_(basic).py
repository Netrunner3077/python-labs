import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))
a = float(input("Введите a: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))

if 0 < x < 1 and 0 < y < 1:
    b = 2 * math.log(x) * max(min(x, y), math.sin(c * x), math.cos(d))
elif x < 0 and y < 0:
    b = min(math.exp(x + 1), y)
else:
    b = a + x

print("Исходные данные:")
print(f"  x = {x}, y = {y}, a = {a}, c = {c}, d = {d}")
print(f"Результат: b = {b}")

f = open("result.txt", "w")
f.write(f"x = {x}\n")
f.write(f"y = {y}\n")
f.write(f"a = {a}\n")
f.write(f"c = {c}\n")
f.write(f"d = {d}\n")
f.write(f"b = {b}\n")
f.close()