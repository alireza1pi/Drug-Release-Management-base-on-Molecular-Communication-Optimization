import numpy as np
import math
import sympy as sym
from scipy.integrate import quad
import matplotlib.pyplot as plt
import functions as f

def Ber_on_ISI_Length():
    Ns=450
    n=Ns
    sh=(5,30)
    ber=np.zeros(sh)
    jj=0
    for ts in [1e-3,3.1e-3,5.3e-3,7.4e-3,16e-3]:

        II=[]
        for I in range(1,31):
            II=II+[I]
            ber[jj][I-1]=f.P_e(n,ts,f.d,I,f.T_max)
        jj=jj+1

    colors=['b','r','g','y','m']
    labels=['ts=1e-3','ts=3.1e-3','ts=5.3e-3','ts=7.4e-3','ts=16e-3']
    for jj in range(5):

        plt.plot(II,ber[jj],color=colors[jj],label=labels[jj])
        plt.xlabel('ISI length') 
        plt.ylabel('BER')
        plt.title("figure 3")
        plt.legend()
    
    return

Ber_on_ISI_Length()