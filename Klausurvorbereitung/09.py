import numpy as np

def newton(x, y):
  amount = len(x)
  coefficients = [y[0]]
  previous_differences = y
  for index in range(amount - 1):
    current_differences = []
    for k in range(amount - index - 1):
      difference = (previous_differences[k + 1] - previous_differences[k]) / (x[k + index + 1] - x[k])
      current_differences.append(difference)
    coefficients.append(current_differences[0])
    previous_differences = current_differences
  return coefficients


def horner_schema(coefficients, x, point):
  total = 0
  amount = len(coefficients)
  for k in range(amount):
    coefficient = coefficients[k]
    product = 1
    for j in range(k):
      product *= (point - x[j])
    total += coefficient * product
  return total

total_amount = 20
x = [(-2+i * (1/5)) for i in range(total_amount)]
y = [np.exp(-(point **2)) for point in x]
for i in range(total_amount):
  print(str(x[i]) + " " + str(y[i]))
coefficients = newton(x, y)
print("Koeffizienten: " + str(coefficients))
point = 8
result = horner_schema(coefficients, x, point)
print("An der Stelle x = 8 gilt: p(x=8)=p(8)=" + str(result))
