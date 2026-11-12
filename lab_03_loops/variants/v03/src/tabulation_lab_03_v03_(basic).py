from math import exp


a = -3
b = 3
h = .4
n = int((b - a) / h + 1e-9) + 1
total = 1.0

with open("result.txt", "w", encoding="utf-8") as file:
    print("x | y")
    file.write("x | y\n")
    for i in range(n):
        x = round(a + i * h, 12)
        if x > 2:
            y = exp(x)
        elif -2 < x < 2:
            y = x + 4
        elif x < -2:
            y = 0
        else:
            y = None
        if y is None:
            row = f"{x:.8g} | не определено"
        else:
            row = f"{x:.8g} | {y:.10g}"
            if y > 0:
                total = total * y
        print(row)
        file.write(row + "\n")
    summary = f"Произведение = {total}"
    print(summary)
    file.write(summary + "\n")
