from math import cos, sin


a = -5
b = 5
h = .4
n = int((b - a) / h + 1e-9) + 1
total = 0.0

with open("result.txt", "w", encoding="utf-8") as file:
    print("x | y")
    file.write("x | y\n")
    for i in range(n):
        x = round(a + i * h, 12)
        if x < 0:
            y = x ** 2 - 1
        elif 0 < x < 1.5:
            y = cos(x)
        elif x > 1.5:
            y = sin(x - 1)
        else:
            y = None
        if y is None:
            row = f"{x:.8g} | не определено"
        else:
            row = f"{x:.8g} | {y:.10g}"
            if y < 0:
                total = total + y
        print(row)
        file.write(row + "\n")
    summary = f"Сумма = {total}"
    print(summary)
    file.write(summary + "\n")
