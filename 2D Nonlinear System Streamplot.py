import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# State space representation
def fx(x):
    dx1_dt = x[1]
    dx2_dt = -9.81 * np.sin(x[0]) - 1.5 * x[1]
    return dx1_dt, dx2_dt

Stationary_points = []

lower = -8 # min
upper =  8 # max
inter = 10 # interpolation points

# Search all the possible solutions by initial point [x1,x2]
for x1 in np.linspace(lower,upper,inter):
    for x2 in np.linspace(lower,upper,inter):
        root = fsolve(fx,[x1,x2])
        if lower <= root[0] <= upper and lower <= root[1] <= upper and not any(np.allclose(root, point) for point in Stationary_points):
            Stationary_points.append(root)

# Streamplot
x1, x2 = np.meshgrid(np.linspace(lower, upper, 2048), np.linspace(lower, upper, 2048))
dx1_dt, dx2_dt = fx([x1,x2])
plt.streamplot(x1, x2, dx1_dt, dx2_dt, density=4.5, linewidth=1, arrowsize=1, arrowstyle='->', minlength=0.02)

# Stationary point plot
for point in Stationary_points:
    plt.scatter(point[0], point[1], color='r', s = 10)

# plot title ans labels
plt.title('Streamplot')
plt.xlabel('x1')
plt.ylabel('x2')

# plot
print(Stationary_points)
plt.show()
