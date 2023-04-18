import random

# Координаты начальной точки
x = 0
y = 0

# Количество часов блуждания крокодила
hours = 10

# Количество прогонов метода Монте-Карло
num_simulations = 1000

# Списки для сохранения координат x и y
x_values = []
y_values = []

# Прогоним метод Монте-Карло
for i in range(num_simulations):
    # Сбросим координаты крокодила в начальную точку
    x = 0
    y = 0

    # Крокодил блуждает определенное число часов
    for j in range(hours):
        # Определяем случайное направление блуждания
        direction = random.choice(['north', 'south', 'east', 'west'])

        # Изменяем координаты в соответствии с направлением
        if direction == 'north':
            y += 1
        elif direction == 'south':
            y -= 1
        elif direction == 'east':
            x += 1
        elif direction == 'west':
            x -= 1

    # Сохраняем полученные координаты
    x_values.append(x)
    y_values.append(y)

# Определяем минимальные и максимальные значения координат
min_x = min(x_values)
max_x = max(x_values)
min_y = min(y_values)
max_y = max(y_values)

# Выводим результаты
print(f"Координаты X: {min_x} - {max_x}")
print(f"Координаты Y: {min_y} - {max_y}")

import matplotlib.pyplot as plt

# Создаем график
fig, ax = plt.subplots()

# Отображаем точки на графике
ax.scatter(x_values, y_values)

# Устанавливаем заголовок и подписи осей
ax.set_title("Крокодил в городе")
ax.set_xlabel("Координата X")
ax.set_ylabel("Координата Y")

# Отображаем график
plt.show()
