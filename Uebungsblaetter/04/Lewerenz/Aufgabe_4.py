"""
Algorithmische Mathematik II - Uebungsblatt Nr. 4
Tutorium Gruppe 8
Abgabe von: Alexander Rohe, Lars Lewerenz
"""
import numpy
from numpy import random
from matplotlib import pyplot


# a)

def random_walk(probability, steps):
  s = []
  current = 0
  s.append(current)
  for _ in range(steps - 1):
    result = -1
    if probability >= random.rand():
      result = 1
    current += result
    s.append(current)
  return s


def plot_walks():
  n = 1000
  p = 0.5
  steps = numpy.array(range(0, n))
  pyplot.figure(figsize=(16, 10))
  for index in range(10):
    walk = random_walk(p, n)
    pyplot.plot(steps, walk)
  pyplot.title("")
  pyplot.show()

# b)

def end_value(probability, steps):
  current = 0
  for _ in range(steps - 1):
    result = -1
    if probability >= random.rand():
      result = 1
    current += result
  return current

def expected_value(probability, steps):
  total = 0
  for _ in range(steps - 1):
    total += probability * 1
    total += (1 - probability) * -1
  return total

def many_walks():
  probabilities = [0.3, 0.5, 0.75]
  n = 100
  colors = [['blue', 'orange'], ['red', 'green'], ['olive', 'purple']]
  for index, p in enumerate(probabilities):
    random_values = []
    for _ in range(10000):
      random_values.append(end_value(p, n))

    expected_values = []
    for _ in range(10000):
      expected_values.append(expected_value(p, n))

    pyplot.hist([random_values, expected_values], color=colors[index], label='p: ' + str(p))

  pyplot.tight_layout()
  pyplot.legend()
  pyplot.show()

plot_walks()
many_walks()