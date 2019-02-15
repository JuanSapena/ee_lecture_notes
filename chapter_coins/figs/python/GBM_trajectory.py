#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:54:25 2018

@author: obp48
"""
import matplotlib.pyplot as plt
import numpy as np
from decimal import * 
import random
import pandas as pd
import pickle

#data_dir='./../../../../../../Dropbox/LML_research/ee_data'

T = 100
dt=0.1
sdt=np.sqrt(dt)
STEPS=int(T/dt)
time=[0]
x=[1]
mu=0.05
sigma=np.sqrt(2*mu)

#ensemble = pd.DataFrame(index=np.arange(0,N_ensemble),columns=np.arange(0,T))
#ensemble.iloc[:,0]=np.zeros(N_ensemble)
#
# T additive repetitions
for step in range(1,STEPS):
    time.append(time[step-1]+dt)
    x.append(x[step-1]*(1+np.random.normal(loc=mu*dt, scale=sigma*sdt)))
#t_ave=ensemble.iloc[0,:].expanding(min_periods=1).mean()
#ensemble.to_pickle(data_dir+"coin_10000.pkl")
#ensemble=pd.read_pickle(data_dir+"coin_ensemble.pkl")

#plt.semilogy(x, np.exp(x*np.log((.6+1.5)/2)), 'lightblue', linewidth=5,label='Mathematical expectation')
plt.plot(time, x, 'b-', label='GBM trajectory')
#plt.plot(x, np.mean(ensemble.iloc[0:100,:]), 'g-', label='$N=100$')
#plt.plot(x, np.mean(ensemble.iloc[0:10000,:]), 'r-', label='$N=10,000$')
#plt.plot(x, np.mean(ensemble), 'k-', label='$N=1,000,000$')
plt.xlim((0,max(time)))
plt.legend()
plt.xlabel('$t$')
plt.ylabel(r'$x(t)$')


plt.savefig("./../GBM_trajectory.pdf", bbox_inches='tight')
plt.show()
