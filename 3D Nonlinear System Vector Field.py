import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


# State space representation
def fx(x):
    dx1_dt = np.sin(np.pi * x[0]) * np.cos(np.pi * x[1]) * np.cos(np.pi * x[2])
    dx2_dt = -np.cos(np.pi * x[0]) * np.sin(np.pi * x[1]) * np.cos(np.pi * x[2])
    dx3_dt = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x[0]) * np.cos(np.pi * x[1]) * np.sin(np.pi * x[2]))
    return dx1_dt, dx2_dt, dx3_dt


# plot boundaries
lower = -5  # min
upper = 5  # max
step = 1  # step size

# Search all the possible solutions by initial point [x1,x2,x3]
Stationary_points = []
# Search all the possible solutions by initial point [x1,x2]
for x1 in np.arange(lower, upper, step):
    for x2 in np.arange(lower, upper, step):
        for x3 in np.arange(lower, upper, step):
            root = fsolve(fx, [x1, x2, x3])
            if lower <= root[0] <= upper and lower <= root[1] <= upper and lower <= root[2] <= upper and \
                    not any(np.allclose(root, point) for point in Stationary_points):
                Stationary_points.append(root)

print(Stationary_points)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1, x2, x3 = np.meshgrid(np.arange(lower, upper, step),
                         np.arange(lower, upper, step),
                         np.arange(lower, upper, step))

dx1_dt, dx2_dt, dx3_dt = fx([x1, x2, x3])

ax.quiver(x1, x2, x3, dx1_dt, dx2_dt, dx3_dt, length=0.8, normalize=True)

for point in Stationary_points:
    plt.scatter(point[0], point[1], color='r', s=10)

ax.set_title('Vector Field')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')

plt.show()
