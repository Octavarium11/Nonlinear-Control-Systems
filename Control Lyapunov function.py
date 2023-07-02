"""
Consider the second-order nonlinear system
x1_dot = −x2
x2_dot = x1 + x2 * u
and the functions
V(x) = 0.5 * x1 **2 + 0.5 * x2 ** 2
"""
from sympy import *
from sympy import symbols
from sympy import Matrix

# System order
n = 2  # fill in


def generate_symbols(n):
    return list(symbols('x:{}'.format(n)))


u = symbols('u')

x = generate_symbols(n)

# State space representation
f_x = Matrix([[-x[1]], [x[0]]])  # fill in

f_x_u = Matrix([[-x[1]], [x[0] + x[1] * u]])  # fill in

g_x = Matrix([[0], [x[1]]])  # fill in

# define Lyapunov function
V = Matrix([0.5 * x[0] ** 2 + 0.5 * x[1] ** 2])

# Varify control Lyapunov function, V_dot_x_u has to be negative definite.
V_dot_x_u = V.jacobian(x) * f_x_u

print("V_dot_x_u: ", simplify(V_dot_x_u[0]))

# Sontag's formula
if V.jacobian(x) * g_x != 0:
    a_x = -1 * (V.jacobian(x) * f_x + ((V.jacobian(x) * f_x) ** 2 + (V.jacobian(x) * g_x) ** 4)) ** 0.5 * (
            V.jacobian(x) * g_x).inv()
else:
    a_x = 0

a_x = powdenest(simplify(a_x[0]),force=True)
print("u = a(x): ", a_x)

# CLF inequality with u = a(x)
V_dot_x_ax = V.jacobian(x) * f_x + V.jacobian(x) * g_x * a_x
V_dot_x_ax = simplify(V_dot_x_ax[0])
print("V_dot_x_ax: ",V_dot_x_ax, "<= 0")

'''
To show asymptotic stability, the invariance principle can be applied: 
∀x1 ̸= 0∧x2 = 0 it follows that M= {0} is the largest pos. inv. set. 
Moreover, D = R^2 holds and V1(x) is pos. def. and radially unbounded, 
thus the system with equilibrium xe = 0 is globally asymptotically stable.
'''