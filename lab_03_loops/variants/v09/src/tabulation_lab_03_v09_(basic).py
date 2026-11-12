from math import pi, sin


a = -pi
b = pi
h = pi/4
n = int((b - a) / h + 1e-9) + 1
total = 0.0

with open("result.txt", "w", encoding="utf-8") as file:
    print("x | y")
    file.write("x | y\n")
    for i in range(n):
        x = a + i * h
        y = 1 / (x + 2 * pi) - sin(x)
        if y is None:
            row = f"{x:.8g} | не определено"
        else:
            row = f"{x:.8g} | {y:.10g}"
            if y > 0:
                total = total + y
        print(row)
        file.write(row + "\n")
    summary = f"Сумма = {total}"
    print(summary)
    file.write(summary + "\n")
