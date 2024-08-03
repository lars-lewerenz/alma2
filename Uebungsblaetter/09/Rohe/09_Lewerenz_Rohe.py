import math
import matplotlib.pyplot as plt

def make_Koefs(x,f):
    if (type(x) != list) or (type(f) != list or len(x) != len(f)):
        print("Bitte zwei gleichlange Listen eingeben!")
        return None

    n = len(x)
    ret = [f[0]]
    difs1 = f

    for i in range(n-1):
        difs2 = []
        for k in range(n-1-i):
            difs2.append((difs1[k+1]-difs1[k]) / (x[k+i+1]-x[k]))
        ret.append(difs2[0])
        difs1 = difs2

    return ret


def Horner(x,f,st):
    Koefs = make_Koefs(x,f)
    ret = 0

    for i in range(len(x)):
        Summand = Koefs[i]
        for k in range(i):
            Summand *= (st - x[k])
        ret += Summand
    
    return ret

#print(Horner([0,1,2,3],[0,1,4,9],4))

x_values = [0.2*i-2 for i in range(21)]
y_values = [math.exp(-(x**2)) for x in x_values]

x_axisa = [0.01*i-2 for i in range(201)]
x_axisb = [0.01*i for i in range(201)]
y_exp = [math.exp(-(x**2)) for x in x_axisa]
y_int = [Horner(x_values,y_values,x) for x in x_axisb]

plt.plot(x_axisa,y_exp, "r", label="Originalfunktion")
plt.plot(x_axisb,y_int, "b", label="Interpolation")
plt.legend()
plt.show()

#Würde man beide aufeinander plotten, wäre nur ein Graph zu sehen.

x_axisc = [0.025*i-2 for i in range(161)]
Differences = [abs( math.exp(-(x**2)) - Horner(x_values,y_values,x)) for x in x_axisc]
plt.semilogy(x_axisc,Differences)
plt.show()