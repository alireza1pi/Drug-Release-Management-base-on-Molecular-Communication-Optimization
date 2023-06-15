############################### functions #############################

import numpy as np
import math
import sympy as sym
from scipy.integrate import quad
import matplotlib.pyplot as plt
## contant variables
r=50e-6
pi=math.pi
e=math.e
pi1=.5
pi0=1-pi1
D=4e-9
d=2e-6
r0=r+d

I=20

sigma2_no=100
sigma2_co=100 
mu_no=100   
n_aa=51
r_unit=10e-6
r_mm=2.5e-9
r_v=.05e-6
N_max=800
ts_min=1e-3
T_max=20e-2

E_T_max=1000e6

## other parameters
#D=(KB*T)/(6*pi*eta*RH)


def f_hit(t):
    y=(r*(r0-r))/(r0*math.sqrt(4*math.pi*D*(t**3)))
    return y 
                  
def erf(x):
    def integrand(u):
        return (1/math.sqrt(2*math.pi))*math.exp(-(u**2))
    s8, err=quad(integrand,0,x)
    return s8

def F_hit(t):
    y=(r/r0)*erf((r-r0)/math.sqrt(4*D*t))
    return y
    
def pi(i,ts):
    y=F_hit(i*ts)-F_hit(ts*(i-1))
    return y

def P_hit(d,ts):
    y=(r/(r+d))*erf(d/(math.sqrt(4*D*ts)))
    return y

def xs(n):
    y=n%2   
    return y

def N_c(n,ts,d,I,T_max):
    y=np.random.binomial(n*xs(n), P_hit(d,ts))  
    return y

def N_p(n,ts,d,I,T_max):
    y=0
    for i in range(1,I+1):
        y=y+np.random.binomial(n*xs(n-1),(P_hit(d, i*ts)-P_hit(d, ts)))
    return y

def N_no(n):
    y=np.random.normal(mu_no,sigma2_no)
    return y
        
def N_co(n):
    y=np.random.normal(0,sigma2_co)
    return y

def N_T(n,ts,d,I,T_max):
    y=N_c(n,ts,d,I,T_max)+N_p(n,ts,d,I,T_max)+N_no(n)+N_co(n)
    return y
    
def mu0(n,ts,d,I,T_max):
    sigma_qi=0
    for i in range(1,I+1):
        sigma_qi=sigma_qi+(P_hit(d, (i+1)*ts)-P_hit(d, i*ts))
    y=pi1*n*sigma_qi+mu_no
    return y


def mu1(n,ts,d,I,T_max):
    sigma_qi=0
    for i in range(1,I+1):
        sigma_qi=sigma_qi+(P_hit(d, (i+1)*ts)-P_hit(d, i*ts))
    y=pi1*n*sigma_qi+n*P_hit(d, ts)+mu_no
    return y


def sigma20(n,ts,d,I,T_max):
    sigma_qii=0
    for i in range(1,I+1):
        sigma_qii=sigma_qii+((P_hit(d, (i+1)*ts)-P_hit(d, i*ts))*(1-(P_hit(d, (i+1)*ts)-P_hit(d, i*ts))))
    sigma_qi2=0
    for i in range(1,I+1):
        sigma_qi2=sigma_qi2+((P_hit(d, (i+1)*ts)-P_hit(d, i*ts))**2)
    y=pi1*n*sigma_qii+pi0*pi1*n**2*sigma_qi2+sigma2_no+mu0(n,ts,d,I,T_max)
    return y
def sigma21(n,ts,d,I,T_max):
    sigma_qii=0
    for i in range(1,I+1):
        sigma_qii=sigma_qii+((P_hit(d, (i+1)*ts)-P_hit(d, i*ts))*(1-(P_hit(d, (i+1)*ts)-P_hit(d, i*ts))))
    sigma_qi2=0
    for i in range(1,I+1):
        sigma_qi2=sigma_qi2+((P_hit(d, (i+1)*ts)-P_hit(d, i*ts))**2)
    y=n*P_hit(d, ts)*(1-P_hit(d, ts))+pi1*n*sigma_qii+pi0*pi1*n**2*sigma_qi2+sigma2_no+mu1(n,ts,d,I,T_max)
    return y

def ta_D(n,ts,d,I,T_max):
    A=1/sigma20(n,ts,d,I,T_max)-1/sigma21(n,ts,d,I,T_max)
    B=mu1(n,ts,d,I,T_max)/sigma21(n,ts,d,I,T_max)-mu0(n,ts,d,I,T_max)/sigma20(n,ts,d,I,T_max)
    gg=sym.sqrt(sigma21(n,ts,d,I,T_max))/sym.sqrt(sigma20(n,ts,d,I,T_max))
    ggg=sym.exp(.5*(((mu1(n,ts,d,I,T_max)**2)/sigma21(n,ts,d,I,T_max))-((mu0(n,ts,d,I,T_max)**2)/sigma20(n,ts,d,I,T_max))))
    C=((pi0/pi1)*(gg))*(ggg)
    y=(sym.sqrt(B**2+2*A*sym.ln(C))-B)/A
    return y

def x_hat_d(n,ts,d,I,T_max):
    if N_T(n)>= ta_D(n,ts,d,I,T_max):
        y=1
    elif N_T(n)<ta_D(n,ts,d,I,T_max):
        y=0
    return y
            
    

def P_e(n,ts,d,I,T_max):
    #y=pi1*(1/2)*(1+erf((ta_D-mu1(n,ts,d,I,T_max))/math.sqrt(2*sigma21(n,ts,d,I,T_max))))+pi0*(1/2)*(1-erf((ta_D-mu0(n,ts,d,I,T_max))/math.sqrt(2*sigma20(n,ts,d,I,T_max))))
    y=1/2+1/4*(erf((ta_D(n,ts,d,I,T_max)-mu1(n,ts,d,I,T_max))/math.sqrt(2*sigma21(n,ts,d,I,T_max)))-erf((ta_D(n,ts,d,I,T_max)-mu0(n,ts,d,I,T_max))/math.sqrt(2*sigma20(n,ts,d,I,T_max))))
    return y


Cv=(r_v/(r_mm*math.sqrt(3)))**3
E_S=202.88*(n_aa-1)
E_V=83*5*(4*math.pi*r_v**2)
E_C=83*math.floor((r_unit/2)/8)
E_E=830


#E_T=n*E_S+np.floor(n/Cv)*(E_V+E_C+E_E)
def E_T(n):
    y=202.88*(n_aa-1)*n+np.floor(n/Cv)*((83*5*(4*math.pi*(r_v**2)))+83*np.floor((r_unit/2)/8)+830)
    return y


############################# optimization ##############################
def Pe_time():
    N_max=800
    j=0
    sh=(4,16)
    tss=np.zeros(sh)
    ber=np.zeros(sh)
        
    for n in [150,250,500,750]:
        
       
        if E_T(n)<=E_T_max:
            for i in range(1,17):
                ts=.001*i  
                tss[j][i-1]=ts
                ber[j][i-1]=P_e(n, ts)
        j=j+1
    print(tss[1])
        
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
                

def Ber_on_distance():
    Ns=450
    n=Ns
    ts=15e-6
    dd=14
    ber=[]
    dis=[]
    for i in range(4):
        ddd=dd+i
        d=ddd*(10**(-6))
        ber=ber+[P_e(n, ts)]
        dis=dis+[d]
    print(dis)
    print(d)
    print(ber)
    return            


        
    

            
            
                
        
    







