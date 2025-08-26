import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])


n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)


a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
b = y_mean - a * x_mean


x_pred = np.linspace(1, 5, 100)
y_pred = a * x_pred + b


plt.scatter(x, y, color='blue', label='Data')
plt.plot(x_pred, y_pred, color='green', label='Regression') 
plt.legend()
plt.title("Linear regression")
plt.show()
