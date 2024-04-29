import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# �������� ������ ���� ���������
fig, ax = plt.subplots()

# ������������� ������� ���������
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# ������� ������ ������ ��� ������� �������������� ������
line, = ax.plot([], [], lw=2)

# ������� ��� ������������� ��������
def init():
    line.set_data([], [])
    return line,

# �������, ������� ����� ���������� �� ������ ���� ��������
def animate(i):
    x = np.linspace(0, 10, 100)
    y = np.sin(x - 0.1*i) * np.cos(x - 0.1*i) # ������ �������������� ������ (���������)
    line.set_data(x, y)
    return line,

# �������� ��������
ani = FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)

# ���������� �������� � ����
ani.save('geometry_animation.gif', writer='pillow', fps=30)

# �������� ��������
plt.show()

