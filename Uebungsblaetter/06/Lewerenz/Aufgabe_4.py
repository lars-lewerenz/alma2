"""
Algorithmische Mathematik II - Uebungsblatt Nr. 6
Tutorium Gruppe 8
Abgabe von: Alexander Rohe, Lars Lewerenz
"""

import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(n_samples):
  x, y = np.random.rand(2, n_samples)
  # modelliert chi
  inside_circle = np.sum(x**2 + y**2 <= 1)
  return (inside_circle / n_samples) * 4

def root_mean_square_error(n_samples, n_trials=100):
  errors = []
  for _ in range(n_trials):
    pi_approx = monte_carlo_pi(n_samples)
    errors.append((pi_approx - np.pi)**2)
  return np.sqrt(np.mean(errors))

n_values = [10**i for i in range(1, 6)]
rmse_values = [root_mean_square_error(n) for n in n_values]

plt.figure(figsize=(10, 6))
plt.loglog(n_values, rmse_values, marker='o')
plt.xlabel('Stichproben (log.)')
plt.ylabel('RMSE (log.)')
plt.title('RMSE von Monte Carlo π Approximation')
plt.grid(True)
plt.show()