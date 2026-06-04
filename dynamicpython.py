import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 0.5*x**3 - 2*x**2 + 3*x + 1

x = np.linspace(-2, 4, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = 0.5x^3 - 2x^2 + 3x + 1')
plt.grid(True)
plt.show()