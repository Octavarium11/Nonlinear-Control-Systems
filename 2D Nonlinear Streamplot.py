import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, sin, pi, S

# State space representation
def fx(x1, x2):
    dx1_dt = -x1**3 + x2
    dx2_dt = x1*x2 - 1
    return dx1_dt, dx2_dt

# create grid
a = -5 # min
b =  5 # max
x1, x2 = np.meshgrid(np.linspace(a, b, 512), np.linspace(a, b, 512))

# Calculate derivatives
dx1_dt, dx2_dt = fx(x1, x2)

# Streamplot
plt.streamplot(x1, x2, dx1_dt, dx2_dt, density=5, linewidth=0.8, arrowsize=1, arrowstyle='->', minlength=0.02)

# Solve and plot stationary points
x1, x2 = symbols('x1 x2', real=True)
equations = [Eq(-x1**3+x2, 0), Eq(x1*x2-1, 0)] # type equations in the function fx
solutions = solve(equations, (x1, x2))

"""
# case: append other solutions for sine and cosine
n_values = range(math.ceil(-a/pi), b//pi)

for n in n_values:
    x1_solution = n * pi
    if x1_solution not in [sol[0] for sol in solutions]: # avoid repeat
        solutions.append((x1_solution, S(0)))  # S(0) is value zero from sympy
"""

print(solutions)

# Point plot
for item in solutions:
    a, b = item
    plt.plot(a, b, 'o')

# title
plt.title('Streamplot')
plt.xlabel('x1')
plt.ylabel('x2')

# plot
plt.show()