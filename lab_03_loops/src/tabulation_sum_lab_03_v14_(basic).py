import math
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = RESULTS_DIR / "result_lab_3_v14.txt"

x_start = float(input("Введите начало отрезка: "))
x_end = float(input("Введите конец отрезка: "))
step = float(input("Введите шаг: "))

if step <= 0:
    print("Ошибка: шаг должен быть положительным.")
    exit(1)
if x_end < x_start:
    print("Ошибка: конец отрезка должен быть не меньше начала.")
    exit(1)

n = int(round((x_end - x_start) / step)) + 1
total = 0.0

header = f"{'x':>10} | {'y':>14}"
sep = "-" * len(header)
print(header)
print(sep)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(header + "\n")
    f.write(sep + "\n")

    for i in range(n):
        x = x_start + i * step

        if x < 0:
            y = x * x - 1
        elif x < 1.5:
            y = math.cos(x)
        else:
            y = math.sin(x - 1)

        print(f"{x:>10.4f} | {y:>14.6f}")
        f.write(f"{x:>10.4f} | {y:>14.6f}\n")

        if y > 0:
            total = total + y

    print(sep)
    print(f"Сумма положительных y = {total:.6f}")
    f.write(sep + "\n")
    f.write(f"Сумма положительных y = {total:.6f}\n")

print(f"\nРезультат сохранён: {OUTPUT_FILE}")