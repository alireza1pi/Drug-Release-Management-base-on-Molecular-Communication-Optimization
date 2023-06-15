import numpy as np
import matplotlib.pyplot as plt
import functions as f

colors=['b','r','y','m']
labels=['d=1e-6','d=1e-5','d=1e-4','d=3e-4']

ts=1e-6
I=f.I
T_max=f.T_max
jj=0
for ii in [1,10,100,300]:
    d=ii*10**-6
    ber=[]
    NN=[]
    for n in range(1,799):
        a=f.P_e(n, ts, d, I, T_max)
        NN=NN+[n]
        ber=ber+[a]
        
    plt.plot(NN,ber,color=colors[jj],label=labels[jj])
    plt.xlabel('Ns') 
    plt.ylabel('Ber')
    plt.title("fig 5")
    plt.legend()
    jj=jj+1