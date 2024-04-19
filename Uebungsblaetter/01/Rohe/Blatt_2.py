import matplotlib.pyplot as plt
import scipy

"""Aufgabenteil a"""

def LCG(peri, seed, numbers):
    if type(peri) != list or len(peri) != 3:
        print("Die Eingabedaten sind falsch!")
        return(None)
    a = peri[0]
    c = peri[1]
    m = peri[2]
    ret = []
    for i in range(numbers):
        seed = (a*seed+c)%m
        ret.append(seed/m)
    return ret

random = LCG([11,0,63], 1, 10000)
ZX81_LCG = LCG([75, 0, 2**16+1], 1, 10000)
RANDU_LCG = LCG([65539, 0, 2**31], 1, 10000)

def plot_a(li):
    le = len(li)
    tupels = []
    lix = li[:le-1]
    liy = li[1:]
    plt.scatter(lix, liy)
    plt.show()

#plot_a(random)
#plot_a(ZX81_LCG)
#plot_a(RANDU_LCG)
    
#Für die erst Verteilung gibt es offensichtlich 
#nur 6 Werte, die Verteilung ist also sehr schlecht.
#Bei ZX81 liegen die Werte auf parallelen Geraden 
#(was schon besser ist, aber immer noch nicht optimal)
#und bei RANDU völlig chaotisch. Daher ist RANDU wohl
#der beste der drei Generatoren.
    

"""Aufgabenteil b"""

def random_to_binomial(zahlen, k):
    ret = []
    borders = []
    a = 0
    for i in range(k + 1):
        borders.append(((scipy.special.binom(k, i)) / 2**k) + a)
        a = borders[i]
    print(borders)
    for z in zahlen:
        b = 0
        while z > borders[b]:
            b += 1
        ret.append(b)
    return ret

plt.hist(random_to_binomial(RANDU_LCG, 10))
plt.show()