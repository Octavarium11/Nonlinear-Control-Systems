from sympy import *
from sympy import symbols
from sympy import Matrix

# System order
n = 2  # fill in


def generate_symbols(n):
    return list(symbols('x:{}'.format(n)))


x = generate_symbols(n)

# State space representation
f = Matrix([[-x[0] + x[1] ** 2], [-x[1] - x[0] ** 3]])  # fill in

# symmetric, positive definite matrices P, R ∈ R^n
P = Matrix([[1, 0], [0, 1]])  # fill in
R = Matrix([[1, 0], [0, 1]])  # fill in


# Jacobian matrix
def Ax():
    return Matrix([f.jacobian(x)])


Ax = Ax()


# Generalized Krasovskii function F(x), F(x) has to be negative definite
def Fx():
    return Ax.transpose() * P + P * Ax + R


Fx = Fx()

# Varify the definiteness of F(x) by eigenvalue
eigenvalues = Fx.eigenvals()
for eigenvalue, multiplicity in eigenvalues.items():
    print(f'Eigenvalue: {eigenvalue}, Multiplicity: {multiplicity}')

# Varify the definiteness of F(x) by principle minors
principle_minors = []

for i in range(1, n + 1):
    principle_minors.append(Fx[:i, :i].det())
    print("%d-th order principle minors: " % i, Fx[:i, :i].det())

print("Principle minors: ",principle_minors)

# Lyapunov function
def V():
    return f.transpose() * f


V = simplify(V()[0])

print("Fx = ", Fx)
print("V(x) = ", V)
