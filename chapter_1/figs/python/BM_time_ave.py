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

T = 10000
N_ensemble=1

ensemble = pd.DataFrame(index=np.arange(0,N_ensemble),columns=np.arange(0,T))
ensemble.iloc[:,0]=np.zeros(N_ensemble)
#
# T additive repetitions
for t in range(1, T):
    old=ensemble.iloc[0,t-1]
    new=Decimal(old)+Decimal(np.random.choice([-1., 1.]))
    ensemble.iloc[0,t]=new
t_ave=ensemble.iloc[0,:].expanding(min_periods=1).mean()
#ensemble.to_pickle(data_dir+"coin_10000.pkl")
#ensemble=pd.read_pickle(data_dir+"coin_ensemble.pkl")

x = np.arange(T)
#plt.semilogy(x, np.exp(x*np.log((.6+1.5)/2)), 'lightblue', linewidth=5,label='Mathematical expectation')
plt.plot(x, t_ave, 'b-', label='Finite-time average')
#plt.plot(x, np.mean(ensemble.iloc[0:100,:]), 'g-', label='$N=100$')
#plt.plot(x, np.mean(ensemble.iloc[0:10000,:]), 'r-', label='$N=10,000$')
#plt.plot(x, np.mean(ensemble), 'k-', label='$N=1,000,000$')
plt.xlim((0,max(ensemble.columns)))
plt.legend()
plt.xlabel('$t$')
plt.ylabel(r'$\overline{x}_t$')


plt.savefig("./../BM_time_ave.pdf", bbox_inches='tight')
plt.show()
