############################# optimization ##############################

import numpy as np
import pandas as pd
import functions as f
import math



def optimization():   
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
            
    sh=(800,16)
    Q=np.zeros(sh)
    
    i=np.random.randint(2,797)
    j=np.random.randint(2,10)
    
    print('random position is =' ,i ,j )
    print('optimizing...')
    
    Q[i][j]=env[i][j]
    def getAllPossibleNextAction(i,j):
        
        global step_matrix
        if i==0:
            step_matrix=np.zeros((2,3))
            for z in range(2):
                for k in range(3):
                    step_matrix[z][k]=env[i+z][j-1+k]
        elif i==799:
            step_matrix=np.zeros((2,3))
            for z in range(2):
                for k in range(3):
                    step_matrix[z][k]=env[i-2+z][j-1+k]
        elif i==798:
            step_matrix=np.zeros((2,3))
            for z in range(2):
                for k in range(3):
                    step_matrix[z][k]=env[i-2+z][j-1+k]
        elif j==0:
            step_matrix=np.zeros((3,2))
            for z in range(3):
                for k in range(2):
                    step_matrix[z][k]=env[i-1+z][j+k]
        elif j==15:
            step_matrix=np.zeros((3,2))
            for z in range(3):
                for k in range(2):
                    step_matrix[z][k]=env[i-1+z][j-1+k]
            
        elif i<798:              
            step_matrix=np.zeros((3,3))
            for z in range(3):
                for k in range(3):
                    step_matrix[z][k]=env[i-1+z][j-1+k]
                    
        action = []
        max_ind = np.unravel_index(np.argmax(step_matrix, axis=None), step_matrix.shape)
        
        
        
        if env[i][j]==np.amax(env) and env[i][j]==env[i-1][j]:
            action.append('-1')
        elif np.amax(step_matrix)==env[i][j]:
            if np.amax(step_matrix)<np.amax(env):
                action.append('eq')
            else:
                action.append('eq1')
        
        if max_ind[0]==0 and max_ind[1]==1:
            action.append('n_n')
            
        elif max_ind[0]==0 and max_ind[1]==0:
            action.append('w_n')
        elif max_ind[0]==0 and max_ind[1]==2:
            action.append('e_n')
        elif max_ind[0]==1 and max_ind[1]==0:
            action.append('w_w')
        elif max_ind[0]==1 and max_ind[1]==1:
            action.append('c_c')
        elif max_ind[0]==1 and max_ind[1]==2:
            action.append('e_e')
        elif max_ind[0]==2 and max_ind[1]==0:
            action.append('w_s')
        elif max_ind[0]==2 and max_ind[1]==1:
            action.append('s_s')
        elif max_ind[0]==2 and max_ind[1]==2:
            action.append('e_s')
            
        return (action)
    
    for ep in range(1000):    
        action=getAllPossibleNextAction(i, j)
        if action[0]=='-1':
            i=i-1
            
        elif action[0]=='eq':
            i=i+1
            j=j
        if action[0]=='eq1':
            i=i-1
            j=j
        elif action[0]=='n_n':
            i=i-1
            j=j
        elif action[0]=='w_n':
            i=i-1
            j=j-1
        elif action[0]=='e_n':
            i=i-1
            j=j+1
        elif action[0]=='w_w':
            i=i
            j=j-1
        elif action[0]=='c_c':
            if env[i-1][j]<np.amax(env):
                i=i+1
            
            else:
                Ns=i+1
                ts=(j+1)*10**-6
                episode=ep
                print('Ns=',Ns)
                print('ts=',ts)
                print('Episode=',episode)
                break
        elif action[0]=='e_e':
            i=i
            j=j+1
        elif action[0]=='w_s':
            i=i+1
            j=j-1
        elif action[0]=='s_s':
            i=i+1
            j=j
        elif action[0]=='e_s':
            i=i+1
            j=j+1
        if i==800 :
            i=i-1
        if i==799 :
            i=i-1
        if j<0:
            j=0
        if i==np.unravel_index(np.argmax(env, axis=None), env.shape)[0]:
            Ns=i+2
            ts=(j+1)*10**-6
            episode=ep
            
            break
       
        Q[i][j]=env[i][j]
    episode=ep
    ts=(j+1)*10**-6
    Ns=i+1
    print('\n')
    print('Q_tqble is:\n')
    print('Ns=',Ns)
    print('ts=',ts)
    print('Episode=',episode)
    
    
    
    return Ns,ts
optimization()