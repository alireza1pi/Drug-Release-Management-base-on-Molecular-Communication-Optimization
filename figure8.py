################################ figure Ns on reward ################

import numpy as np
import math
import sympy as sym
from scipy.integrate import quad
import matplotlib.pyplot as plt
import functions as f
colors=['','b','','r','','','g','','y','','','','m']
labels=['','ts=1e-6','','ts=3e-6','','','ts=6e-6','','ts=8e-6','','','','ts=12e-6']
d=f.d
T_max=f.T_max
I=f.I
table=(800,16)
env=np.zeros(table)
print('training...')
for n in range (1,f.N_max+1):
    if f.E_T(n)<=f.E_T_max:    
        for i in range(1,17):        
            ts=.001*i             
            ss=0
            for ii in range(1,21):
                ss=ts+ss
            if ss<=f.T_max:
                P_new=np.floor(f.P_e(n, ts,f.d,f.I,f.T_max)*100)/100
                reward=np.floor(math.exp(1/P_new)*100)/100
                env[n-1][i-1]=np.floor(reward*100)/100                
            else:
                env[n-1][i-1]=0

    else:
        env[n-1][:]=0
for v in [1,3,6,8,12]:
    N=[]
    rew=[]
    ts=v*10**-6
    
    for n in range(1,799):
        b=env[n][v-1]
        N=N+[n]
        rew=rew+[b]
    plt.plot(N,rew,color=colors[v],label=labels[v])
    plt.xlabel('Ns') 
    plt.ylabel('reward')
    plt.title("fig 8")
    plt.legend()