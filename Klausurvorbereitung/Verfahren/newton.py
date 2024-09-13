import math

import numpy


def f(x):
  return x**2 - 100

def f_prime(x):
  return 2 * x

def newton_zero(a, eps=1e-200):
  current = a
  iterations = 0
  while True:
    d = - (f(current) / f_prime(current))
    current = current + d
    iterations += 1
    print(current)
    if abs(f(current)) <= eps:
      break
  return iterations, current

print(newton_zero(5099909999990))