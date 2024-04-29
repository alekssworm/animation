import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Создание нового окна рисования
fig, ax = plt.subplots()

# Устанавливаем пределы координат
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Создаем пустой объект для будущей геометрической фигуры
line, = ax.plot([], [], lw=2)

# Функция для инициализации анимации
def init():
    line.set_data([], [])
    return line,

# Функция, которая будет вызываться на каждом шаге анимации
def animate(i):
    x = np.linspace(0, 10, 100)
    y = np.sin(x - 0.1*i) * np.cos(x - 0.1*i) # Пример геометрической фигуры (синусоида)
    line.set_data(x, y)
    return line,

# Создание анимации
ani = FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)

# Сохранение анимации в файл
ani.save('geometry_animation.gif', writer='pillow', fps=30)

# Показать анимацию
plt.show()

