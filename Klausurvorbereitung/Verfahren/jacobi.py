import numpy
import numpy as np

def iterative(a, x, b):
  left = np.tril(a, -1)
  right = np.triu(a, 1)
  diagonal = np.diag(np.diag(a))
  t = np.matmul(-np.linalg.inv(diagonal), np.add(right, left))
  c = np.matmul(np.linalg.inv(diagonal), b)
  print("A: " + str(np.array(a)))
  print("L: " + str(left))
  print("R: " + str(right))
  print("D: " + str(diagonal))
  print("c: " + str(c))
  print("T: " + str(t))
  iterations = 0
  while True:
    x = np.add(np.matmul(t, x), c)
    print("X:" + str(x))
    iterations += 1
    if abs(np.linalg.norm(np.subtract(np.matmul(a, x), b))) < 1e-5:
      break
  print("Iterations: " + str(iterations))
  print("X: " + str(x))


iterative(np.array([[16, 3],[7, -11,]]), np.array([1, 1]), np.array([11, 1993]))