a = -2
b = 2
h = .2
n = int((b - a) / h + 1e-9) + 1
total = 1.0

with open("result.txt", "w", encoding="utf-8") as file:
    print("x | y")
    file.write("x | y\n")
    for i in range(n):
        x = round(a + i * h, 12)
        y = x ** 4 + x ** 3 - 10 * x ** 2 - 34 * x - 25
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
