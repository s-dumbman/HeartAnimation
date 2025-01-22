import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#2023.12.21
# D + 400
#2025.01.23
def machine(a, x):
    return abs(x)**(2/3) + (0.9) * ((3.3 - x**2)**(1/2)) *np.sin(a*np.pi*x)-1

def update(frame):
    global a, direction
    if a >= 26.5:
        direction = -1
    elif a <= 0:
        direction = 1
    if direction == 1:
        a += 0.25
    elif direction == -1:
        a -= 1.25
    print(f"{direction} | {a}")
    y = machine(a, x)
    line.set_ydata(y)
    return line

def plot_function():
    global x, line, a, direction 
    x = np.linspace(-5, 5, 1000)
    a = 0
    direction = 1

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color='black', linewidth=0.1, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.1, linestyle='--')
    ax.grid(color='black', linestyle='--', linewidth=0.1)
    ax.set_title("D+400")

    ax.set_xlim([-2, 2])
    ax.set_ylim([-2.75, 2])

    y = machine(a, x)
    global line
    line, = ax.plot(x, y, color="red", label="Heart Curve")
    ax.legend()

    ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)

    plt.show()

if __name__ == "__main__":
    plot_function()
