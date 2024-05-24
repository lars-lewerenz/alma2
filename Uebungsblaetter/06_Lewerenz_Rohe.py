import random
import matplotlib.pyplot as plt
import math
import numpy as np

def einzelner_Wert():
    x = random.random()
    y = random.random()
    if x**2 + y**2 > 1:
        return 0
    else:
        return 1
    
def approx_pi(n):
    count = 0
    for i in range(n):
        count += einzelner_Wert()
    return 4*(count / n)

def calc_rmse(n):
    r = 0
    for i in range(100):
        r += (approx_pi(n) - math.pi)**2
    return math.sqrt(r/100)

x_axis = [10**(i+1) for i in range(5)]
y_axis = [calc_rmse(x) for x in x_axis]

print(x_axis)
print(y_axis)

plt.loglog(x_axis, y_axis)
plt.show()