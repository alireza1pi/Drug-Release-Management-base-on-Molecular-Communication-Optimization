import numpy as np
import math
import sympy as sym
from scipy.integrate import quad
import matplotlib.pyplot as plt
import functions as f
import optimization as op
def Ns_ts_on_Tmax():
    j=0
    sh=(5,25)
    Nss=np.zeros(sh)
    tss=np.zeros(sh)

    for d in[10e-6,20e-6,3e-6,4e-6,5e-6]:
        TT=[]
        for i in range(1,26):
            T_max=i/100
            [nn,tt]=op.optimization()
            Nss[j][i-1]=nn
            tss[j][i-1]=tt
            TT=TT+[i]
        j=j+1

    colors=['b','r','g','y','m']
    labels=['d=10e-6','d=20e-6','d=30e-6','d=40e-6','d=50e-6']
    for jj in range(5):

        plt.plot(TT,Nss[jj],color=colors[jj],label=labels[jj])
        plt.xlabel('T_max') 
        plt.ylabel('Ns')
        plt.title("figure 6")
        plt.legend()
    plt.show()

    for jj in range(5):

        plt.plot(TT,tss[jj],color=colors[jj],label=labels[jj])
        plt.xlabel('T_max') 
        plt.ylabel('ts')
        plt.title("figure 7")
        plt.legend()
    plt.show()
    return()




Ns_ts_on_Tmax()

