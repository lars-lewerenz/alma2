"""
Algorithmische Mathematik II - Uebungsblatt Nr. 11
Tutorium Gruppe 8
Abgabe von: Alexander Rohe, Lars Lewerenz
"""

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

# Parameter
n = 100
lambda_ = 0.1
tolerance = 10**(-5)

# Funktion g(y) und deren Ableitung g'(y)
def g(y):
  return np.exp(y / (1 + 2 * y))

def g_prime(y):
  return np.exp(y / (1 + 2 * y)) * (1 / (1 + 2 * y) - 2 * y / (1 + 2 * y)**2)

# Berechnung von F(y)
def compute_F(y):
  F = np.zeros(n)
  F[0] = 2 * y[0] - y[1] - 1 - lambda_ * g(y[0])
  F[-1] = -y[-2] + 2 * y[-1] - 1 - lambda_ * g(y[-1])
  for i in range(1, n-1):
    F[i] = -y[i-1] + 2 * y[i] - y[i+1] - lambda_ * g(y[i])
  return F

# Berechnung der Jacobian-Matrix J_F(y)
def compute_jacobian(y):
  main_diag = np.full(n, 2) - lambda_ * g_prime(y)
  off_diag = np.full(n-1, -1)
  diagonals = [main_diag, off_diag, off_diag]
  J = diags(diagonals, [0, 1, -1], format='csr')
  return J

# Newton-Verfahren zur Lösung des nichtlinearen Gleichungssystems
def newton_method():
  y = np.zeros(n)
  iteration = 0

  while True:
    F_val = compute_F(y)
    norm_F = np.linalg.norm(F_val, np.inf)
    print(f'Iteration {iteration}: ||F(y)||_∞ = {norm_F}')

    if norm_F < tolerance:
      break

    J = compute_jacobian(y)
    delta_y = spsolve(J, -F_val)
    y += delta_y
    iteration += 1

  return y

# Lösung des Gleichungssystems
solution = newton_method()

# Plotten der Ergebnisse
plt.plot(range(1, n+1), solution, marker='o')
plt.xlabel('Index i')
plt.ylabel('Lösung y_i')
plt.title('Näherungslösung des nichtlinearen Gleichungssystems')
plt.grid(True)
plt.show()