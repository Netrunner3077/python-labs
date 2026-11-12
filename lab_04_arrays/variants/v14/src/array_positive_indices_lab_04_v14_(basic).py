import random

random.seed(14)

k = 90
z1 = -50
z2 = 20
n = 10
m = 9

B = []
for i in range(k):
    B.append(random.randint(z1, z2))

print("Исходная матрица:")
for i in range(n):
    for j in range(m):
        print(f"{B[i * m + j]:>5}", end="")
    print()

print("\nНомера положительных элементов массива:")
count = 0
for i in range(k):
    if B[i] > 0:
        count = count + 1
        print(f"B[{i}] (номер {i + 1}) = {B[i]}")

print(f"\nВсего положительных элементов: {count}")