"""
Algorithmische Mathematik II - Uebungsblatt Nr. 1
Tutorium Gruppe 8
Abgabe von: Alexander Rohe, Lars Lewerenz
"""


# a)

def lcg(a, c, m, seed):
  return (a * seed + c) % m


def lcgs(a, c, m, start_seed, amount):
  figures = []
  last_seed = start_seed
  while len(figures) < amount:
    next_seed = lcg(a, c, m, last_seed)
    figures.append(to_decimal_form(next_seed))
    last_seed = next_seed
  return figures


def to_decimal_form(number):
  num_digits = len(str(abs(number)))
  divisor = 10 ** num_digits
  return number / divisor


print(lcgs(11, 0, 63, 1, 10_000))
print(lcgs(75, 0, 2 ** 16 + 1, 1, 10_000))
print(lcgs(65539, 0, 2 ** 31, 1, 10_000))

# b)
