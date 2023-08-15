import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Crear la figura y los ejes
fig, ax = plt.subplots()
ax.set_xlim(-200, 200)
ax.set_ylim(-200, 200)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', linewidth=0.5)

# Punto de inicio de la línea
x, y = 0, 0
x=0
y=0

# Radio y ángulo inicial
l1 = 100

angle1 = 0
f1 = 0

q1 = float(input('Ingrese angulo q1: '))
q1_ = np.arange(0.0, q1 + 1, 1)

line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2, color='red')

def init():
    line.set_data([], [])
    return line, line2,

def animate(i):
    global x, y, angle1, angle2, q_, f1, f2
    l1x_new =  l1 * math.cos(math.radians(q1_[angle1]))
    l1y_new =  l1 * math.sin(math.radians(q1_[angle1]))

    line.set_data([x, l1x_new], [y, l1y_new])
    
    
    if q1_[angle1] >= q1:
        f1 = 1
    if f1 == 0:   
        angle1 += 1
    return line, 

ani = animation.FuncAnimation(fig, animate, init_func=init, interval=50, blit=True)

plt.show()
