import numpy as np
import matplotlib.pyplot as mpl


def partial_sum(n, reverse):
  result = 0.0
  if reverse:
    for k in range(n, 0, -1):
      result += 1 / (k ** 4)
  else:
    for k in range(1, n + 1):
      result += 1 / (k ** 4)
  return result


summations = [2 ** k for k in range(1, 21)]


def collect_results():
  forward = [partial_sum(amount, False) for amount in summations]
  backward = [partial_sum(amount, True) for amount in summations]
  return forward, backward


exact = np.pi ** 4 / 90


def collect_diff():
  forward, backward = collect_results()
  forward_diff = [abs(computed - exact) for computed in forward]
  backward_diff = [abs(computed - exact) for computed in backward]
  return forward_diff, backward_diff


def plot_diff():
  forward_diff, backward_diff = collect_diff()
  mpl.loglog(summations, forward_diff, 'o-', label='Vorwärtssummation')
  mpl.loglog(summations, backward_diff, 'x-', label='Rückwärtssummation')
  mpl.title('Abweichung $\\varepsilon_n$ von der exakten Lösung')
  mpl.xlabel('$n$')
  mpl.ylabel('$\\varepsilon_n$')
  mpl.legend()
  mpl.grid(True, which="both", ls="--")
  mpl.savefig('Plot', dpi=900)
  mpl.show()


plot_diff()
