import numpy as np
import matplotlib.pyplot as plt

# Определяем начальные значения параметров модели
N = 1000 # Общее количество учеников в школе
I0 = 10 # Начальное количество зараженных
R0 = 0 # Начальное количество выздоровевших
S0 = N - I0 - R0 # Начальное количество восприимчивых к заражению

beta = 0.2 # Коэффициент заражения
gamma = 0.1 # Коэффициент выздоровления

# Определяем функцию, описывающую изменение состояний во времени
def SIR_model(SIR, beta, gamma):
    S, I, R = SIR
    dS_dt = -beta * S * I / N
    dI_dt = beta * S * I / N - gamma * I
    dR_dt = gamma * I
    return dS_dt, dI_dt, dR_dt

# Определяем параметры для численного решения уравнения
t_max = 100 # Длительность моделирования
dt = 0.1 # Шаг по времени
t = np.linspace(0, t_max, int(t_max/dt) + 1)

# Определяем массивы для хранения значений состояний на каждом временном шаге
S = np.zeros(len(t))
I = np.zeros(len(t))
R = np.zeros(len(t))

# Устанавливаем начальные значения состояний
S[0] = S0
I[0] = I0
R[0] = R0

# Вычисляем значения состояний на каждом временном шаге
for i in range(1, len(t)):
    dS_dt, dI_dt, dR_dt = SIR_model([S[i-1], I[i-1], R[i-1]], beta, gamma)
    S[i] = S[i-1] + dS_dt * dt
    I[i] = I[i-1] + dI_dt * dt
    R[i] = R[i-1] + dR_dt * dt

# Визуализируем результаты моделирования
plt.plot(t, S, label='S(t)')
plt.plot(t, I, label='I(t)')
plt.plot(t, R, label='R(t)')
plt.xlabel('Время (дни)')
plt.ylabel('Количество человек')
plt.legend()
plt.show()