from math import exp


a = .1
b = 1.5
h = .1
n = int((b - a) / h + 1e-9) + 1
total = None

with open("result.txt", "w", encoding="utf-8") as file:
    print("x | y")
    file.write("x | y\n")
    for i in range(n):
        x = round(a + i * h, 12)
        y = x * exp(-x)
        if y is None:
            row = f"{x:.8g} | не определено"
        else:
            row = f"{x:.8g} | {y:.10g}"
            if total is None or y < total:
                total = y
        print(row)
        file.write(row + "\n")
    summary = f"Минимум = {total}"
    print(summary)
    file.write(summary + "\n")
