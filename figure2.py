import numpy as np
import math
import sympy as sym
from scipy.integrate import quad
import matplotlib.pyplot as plt
import functions as f

def Ber_on_distance():
    Ns=450
    n=Ns
    ts=15e-6
    dd_d=2
    dd_u=50
    ber=[]
    dis=[]
    for i in range(dd_u-dd_d):
        ddd=dd_d+i
        d=ddd*(10**(-6))
        ber=ber+[f.P_e(n,ts,d,f.I,f.T_max)]
        dis=dis+[d]

    plt.plot(dis,ber,color='r',label='Ns=450 ts=15e-6')
    plt.xlabel('distance') 
    plt.ylabel('BER')
    plt.title("figure 2")
    plt.legend()
    return           


Ber_on_distance()