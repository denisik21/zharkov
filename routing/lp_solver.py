import sys
from scipy.optimize import linprog

# Чтение данных из аргументов командной строки
n = (len(sys.argv) - 3) // 3  # Вычисляем количество складов

# Извлекаем параметры для каждого склада
costs = [float(sys.argv[1 + i * 3]) for i in range(n)]
times = [float(sys.argv[2 + i * 3]) for i in range(n)]
distances = [float(sys.argv[3 + i * 3]) for i in range(n)]

# Ограничения
max_time = float(sys.argv[-2])
max_distance = float(sys.argv[-1])

# Целевая функция: минимизация стоимости
c = costs

# Матрица ограничений
A = [
    times,       # Ограничение на время
    distances    # Ограничение на расстояние
]

# Правые части ограничений
b = [max_time, max_distance]

# Ограничение на сумму долей маршрутов
A_eq = [[1] * n]
b_eq = [1]

# Ограничения на неотрицательность
bounds = [(0, 1) for _ in range(n)]

# Решение задачи
result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Вывод только оптимального распределения маршрутов
if result.success:
    print(result.x.tolist())
else:
    print("Решение не найдено:", result.message)
