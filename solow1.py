import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

alpha = 0.3
A = 1

def cobb_douglas(K, L, alpha, A):
    return A * (K ** alpha) * (L ** (1 - alpha))

K = np.linspace(1, 100, 100)
L = np.linspace(1, 100, 100)
K, L = np.meshgrid(K, L)

Y = cobb_douglas(K, L, alpha, A)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(K, L, Y, cmap='viridis')

ax.set_title('Cobb-Douglas Production Function')
ax.set_xlabel('Capital (K)')
ax.set_ylabel('Labor (L)')
ax.set_zlabel('Total Production (Y)')
plt.subplots_adjust(left=0.2, right=1.5, top=1.4, bottom=0.1)
plt.show()
