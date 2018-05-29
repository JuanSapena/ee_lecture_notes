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

data_dir='./../../../../../../Dropbox/LML_research/ee_data'

T = 10000
N_ensemble=1

ensemble = pd.DataFrame(index=np.arange(0,N_ensemble),columns=np.arange(0,T))
ensemble.iloc[:,0]=np.ones(N_ensemble)
#
# T multiplicative repetitions
#for t in range(1, T):
#    # 50% chance of 0.6x what we had before, or
#    # 50% chance of 1.5x what we had before.
#    old=ensemble.iloc[0,t-1]
#    new=Decimal(old)*Decimal(np.random.choice([0.6, 1.5]))
#    ensemble.iloc[0,t]=new 
#ensemble.to_pickle(data_dir+"coin_10000.pkl")
ensemble=pd.read_pickle(data_dir+"coin_10000.pkl")

x = np.arange(T)
plt.semilogy(x, np.exp(x*((np.log(.6)+np.log(1.5))/2)), 'lightblue', linewidth=3,label='Time-average growth')
plt.semilogy(x, ensemble.iloc[0,:], 'b-', label='$N=1$')
#plt.plot(x, np.mean(ensemble.iloc[0:100,:]), 'g-', label='$N=100$')
#plt.plot(x, np.mean(ensemble.iloc[0:10000,:]), 'r-', label='$N=10,000$')
#plt.plot(x, np.mean(ensemble), 'k-', label='$N=1,000,000$')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('$x(t)$')


plt.savefig("./../x_of_t_log_10000.pdf", bbox_inches='tight')
plt.show()
