import math

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

denominator = x * (x - y) * (2 * x + y)

if denominator == 0:
    print("Ошибка: знаменатель равен нулю. Функция не определена.")
else:
    numerator = x * math.exp(x * y) + 4 * math.cos(x) ** 2
    
    u = numerator / denominator

    print(f"Значение функции u = {u:.4f}")