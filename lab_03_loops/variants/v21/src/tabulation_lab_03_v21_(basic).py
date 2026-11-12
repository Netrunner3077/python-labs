from math import exp


a = -3
b = 3
h = .3
n = int((b - a) / h + 1e-9) + 1
total = 1.0

with open("result.txt", "w", encoding="utf-8") as file:
    print("x | y")
    file.write("x | y\n")
    for i in range(n):
        x = round(a + i * h, 12)
        if x > 1:
            y = exp(x)
        elif x < 0:
            y = 2 * x - 1
        else:
            y = -1
        if y is None:
            row = f"{x:.8g} | не определено"
        else:
            row = f"{x:.8g} | {y:.10g}"
            if y < 0:
                total = total * y
        print(row)
        file.write(row + "\n")
    summary = f"Произведение = {total}"
    print(summary)
    file.write(summary + "\n")
