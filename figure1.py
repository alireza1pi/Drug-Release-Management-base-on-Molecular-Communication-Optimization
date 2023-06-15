import numpy as np
import math
import sympy as sym
from scipy.integrate import quad
import matplotlib.pyplot as plt
import functions as f

def Pe_time():
    N_max=800
    j=0
    sh=(4,16)
    tss=np.zeros(sh)
    ber=np.zeros(sh)

    for n in [150,250,500,750]:


        if f.E_T(n)<=f.E_T_max:
            for i in range(1,17):
                ts=.001*i  
                tss[j][i-1]=ts
                ber[j][i-1]=f.P_e(n,ts,f.d,f.I,f.T_max)
        j=j+1

    colors=['b','r','g','y']
    labels=['Ns=150','Ns=250','Ns=500','Ns=750']
    for jj in range(4):

        plt.plot(tss[jj],ber[jj],color=colors[jj],label=labels[jj])
        plt.xlabel('time') 
        plt.ylabel('BER')
        plt.title("figure 1")
        plt.legend()
    plt.show()    
    return  

Pe_time()       