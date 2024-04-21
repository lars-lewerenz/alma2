"""
Algorithmische Mathematik II - Uebungsblatt Nr. 1
Tutorium Gruppe 8
Abgabe von: Alexander Rohe, Lars Lewerenz
"""

import matplotlib.pyplot as plt
from scipy.special import binom


# a)

def lcg(a, c, m, seed):
  return (a * seed + c) % m


def lcgs(a, c, m, start_seed, amount):
  figures = []
  last_seed = start_seed
  while len(figures) < amount:
    next_seed = lcg(a, c, m, last_seed)
    figures.append(next_seed / m)
    last_seed = next_seed
  return figures


def plotte_lcg(figures, name):
  n = len(figures)
  x = figures[:n - 1]
  y = figures[1:]
  plt.figure(figsize=(20, 20))
  plt.scatter(x, y)

  plt.xlabel("X_n")
  plt.ylabel("X_(n+1)")
  plt.title("LCG - " + name)
  plt.show()


RANDU_LCG = lcgs(65539, 0, 2 ** 31, 1, 10_000)


# plotte_lcg(lcgs(11, 0, 63, 1, 10_000), "Random LCG")
# plotte_lcg(lcgs(75, 0, 2**16, 1, 10_000), "XZ81 LCG")

# plotte_lcg(RANDU_LCG, "RANDU LCG")

# 1) der erste LCG ist kein guter Zufallsgenerator, da es nur 6 verschiedene Zufallszahlen gibt.
# 2) XZ81 LCG ist schon besser, hat aber parallele Geraden, wodurch ein System entsteht und die Verteilung gewisse Muster aufweist.
# 3) RANDU LCG ist der beste von den dreien, weil die Zufallszahlen sehr chaotisch verteilt sind und insbesondere keine Symmetrie
#    erkennen lassen. Auch gibt es keine besonders dichten Bereiche

# b)

def generate_history_binomially_generated(figures):
  k = 10
  p = 0.5
  intervals = []
  p_i = 0
  for i in range(k + 1):
    ## Probability for i hits in k elements
    intervals.append(binom(k, i) * p ** i * (1 - p) ** (k - i) + p_i)
    p_i = intervals[i]
  history = []
  # basically count how many figures lie in each interval
  for figure in figures:
    index = 0
    while figure > intervals[index]:
      index += 1
    history.append(index)
  return history


plt.xlabel("k")
plt.ylabel("Haeufigkeit von k Treffern")
plt.title("LCG: RANDU - gleichverteilte Binomialverteilung")
plt.hist(generate_history_binomially_generated(RANDU_LCG))
plt.show()
