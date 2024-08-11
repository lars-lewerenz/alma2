import matplotlib.pyplot as plt
import scipy


def lcg(prior, a, c, m):
  return (a * prior + c) % m


def lcgs(start, amount, a, c, m):
  current = start
  figures = [normalize(current, m)]
  for _ in range(amount):
    current = lcg(current, a, c, m)
    figures.append(normalize(current, m))

  return figures


def normalize(figure, m):
  return figure / m


def create_pairs(lcgs):
  x = []
  y = []
  last = 0
  for figure in lcgs:
    if last == 0:
      last = figure
      continue
    x.append(last)
    y.append(figure)
    last = figure
  return x, y


def plot_lcg(figures, label, size):
  x, y = create_pairs(figures)
  plt.scatter(x, y, s=size, label=label, alpha=0.8)


amount = 100_000
seed = 1
first = lcgs(seed, amount, 11, 0, 63)
zx81 = lcgs(seed, amount, 75, 0, 2 ** 16 + 1)
randu = lcgs(seed, amount, 65539, 0, 2 ** 31)

def test_lcgs():
  plt.xlabel("X_n")
  plt.ylabel("X_(n+1)")

  plot_lcg(randu, "RANDU", 6)
  plot_lcg(zx81, "ZX81", 6)
  plot_lcg(first, "RANDOM", 64)
  plt.legend()
  plt.show()


#test_lcgs(10_000)

def generate_binomial_distribution(random_figures):
  p = 1/2
  k = 10
  p_i = 0
  intervals = []
  for i in range(k + 1):
    ## Probability for i hits in k elements plus prior probability
    intervals.append(scipy.special.binom(k, i) * p ** i * (1 - p) ** (k - i) + p_i)
    p_i = intervals[i]
  print(intervals)

  hits = []
  for figure in random_figures:
    index = 0
    # make sure the right border of the interval is excluded
    while figure > intervals[index]:
      index += 1
    hits.append(index)
  return hits

_, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)
axs[0].hist(generate_binomial_distribution(first), label="RANDOM", color = "g")
axs[1].hist(generate_binomial_distribution(randu), label = "RANDU")
axs[2].hist(generate_binomial_distribution(zx81), label = "ZX81", color = "orange")

for ax in axs:
  ax.legend()
plt.show()
