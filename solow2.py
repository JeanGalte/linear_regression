import numpy as np
import matplotlib.pyplot as plt








































# # Defining the model parameters
print("alpha:")
# 0.3 originalement
alpha = 0.3
A = 1
s = 0.2
delta = 0.1
L = 100
T = 50
K0 = 10
# Cobb-Douglas production function
def cobb_douglas(K, L, alpha, A):
    return A * (K ** alpha) * (L ** (1 - alpha))








# # Initializing vectors to store values of K and Y
K = np.zeros(T)
Y = np.zeros(T)
K[0] = K0

# # Simulating capital dynamics over time
for t in range(1, T):
    Y[t-1] = cobb_douglas(K[t-1], L, alpha, A)
    K[t] = K[t-1] + s * Y[t-1] - delta * K[t-1]

# Calculating production in the last period
Y[T-1] = cobb_douglas(K[T-1], L, alpha, A)

k = K / Y 


# Plotting the results
plt.figure(figsize=(14, 7))

# Capital over time
plt.subplot(1, 2, 1)
plt.plot(range(T), K, label='Capital (K)', color='b')
plt.xlabel('Time')
plt.ylabel('Capital')
plt.title('Capital Accumulation Over Time')
plt.grid(True)
plt.legend()

# # Production over time
# plt.subplot(1, 2, 2)
# plt.plot(range(T), Y, label='Production (Y)', color='g')
# plt.xlabel('Time')
# plt.ylabel('Production')
# plt.title('Production Over Time')
# plt.grid(True)
# plt.legend()

# k
plt.subplot(1, 2, 2)
plt.plot(range(T), k, label='capital per output', color='g')
plt.xlabel('Time')
plt.ylabel('Production')
plt.title('k over time')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
