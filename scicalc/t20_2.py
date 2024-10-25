import numpy as np
import matplotlib.pyplot as plt

n = int(input("Input count of vertex: "))

theta = np.linspace(0, 2 * np.pi, 150)
radius = 1
a = radius * np.cos(theta)
b = radius * np.sin(theta)

theta = np.linspace(0, 2 * np.pi, n+1)
c = radius * np.cos(theta)
d = radius * np.sin(theta)
e = np.column_stack((c, d))[:-1]

pi = 0
for i in range(n-1):
    p1 = e[i]
    p2 = e[i + 1]
    u = (p2 - p1)**2
    pi += np.sqrt(u[0] + u[1])
pi += np.sqrt(np.linalg.norm(e[-1] - e[0]))
pi /= 2 * radius

fig, ax = plt.subplots(1)
 
ax.plot(a, b)
ax.plot(c, d)
ax.set_aspect(1)
 
plt.title(f"pi ~ {pi}, vertex: {n}")
plt.show()
time.sleep(1)
plt.close()
time.sleep(0.3)
plt.show()
