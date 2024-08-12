import numpy as np
import matplotlib.pyplot as plt

random = np.random.default_rng()


def random_walk(start, n, p):
  current = start
  values = [start]
  for k in range(1, n):
    if p > random.random():
      current += 1
    else:
      current -= 1
    values.append(current)
  return values


def plot_random_walks(amount, p):
  start = 0
  n = 1000
  for _ in range(amount):
    values = random_walk(start, n, p)
    plt.plot(values)
  plt.show()


def expected_final_value(start, n, p):
  add = 1 * n * p
  subtract = -1 * n * (1 - p)
  # = n * (p + (1-p))
  return start + add + subtract


def end_value_of_random_walk(start, n, p):
  current = start
  for k in range(1, n):
    if p > random.random():
      current += 1
    else:
      current -= 1
  return current


def hist_random_walks():
  amount_of_walks = 10_000
  probabilities = [0.3, 0.5, 0.75]
  n = 1000
  start = 0
  colors = [['blue', 'orange'], ['red', 'green'], ['olive', 'purple']]
  for index, p in enumerate(probabilities):
    random_values = []
    expected_values = []

    for _ in range(amount_of_walks):
      random_values.append(end_value_of_random_walk(start, n, p))
      expected_values.append(expected_final_value(start, n, p))

    plt.hist([random_values, expected_values], color=colors[index], label='p: ' + str(p))

  plt.tight_layout()
  plt.legend()
  plt.show()


#plot_random_walks(10, 0.5)
hist_random_walks()