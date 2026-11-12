from math import cos, sin


a = -2
b = 2
h = .25
n = int((b - a) / h + 1e-9) + 1
total = 0.0

with open("result.txt", "w", encoding="utf-8") as file:
    print("x | y")
    file.write("x | y\n")
    for i in range(n):
        x = round(a + i * h, 12)
        if -1 < x < 1:
            y = sin(x)
        else:
            y = 5 * cos(x)
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
