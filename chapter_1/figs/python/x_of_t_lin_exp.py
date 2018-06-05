#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:54:25 2018

@author: obp48
"""
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import pickle

data_dir='./../../../../../../Dropbox/LML_research/ee_data'
#
#T = 52
#N_ensemble=1000000
#
#ensemble = pd.DataFrame(index=np.arange(0,N_ensemble),columns=np.arange(0,T))
#ensemble.iloc[:,0]=np.ones(N_ensemble)
#
## T multiplicative repetitions
#for t in range(1, T):
#    # 50% chance of 0.6x what we had before, or
#    # 50% chance of 1.5x what we had before.
#    ensemble.iloc[:,t]=ensemble.iloc[:,t-1] * np.random.choice([0.6, 1.5],size=N_ensemble)
#ensemble.to_pickle(data_dir+"coin_ensemble.pkl")
#ensemble=pd.read_pickle(data_dir+"coin_ensemble.pkl")

x = np.arange(T)
plt.plot(x, np.exp(x*(.6+1.5-2)/2), 'lightblue', label='Expectation value', linewidth=4)
plt.plot(x, ensemble.iloc[45,:], 'b-', label='$N=1$')
plt.plot(x, np.mean(ensemble.iloc[0:100,:]), 'g-', label='$N=100$')
plt.plot(x, np.mean(ensemble.iloc[0:10000,:]), 'r-', label='$N=10,000$')
plt.plot(x, np.mean(ensemble), 'k-', label='$N=1,000,000$')
plt.xlim((0,max(ensemble.columns)))
plt.ylim((0,18))
plt.legend()
plt.xlabel('$t$')
plt.ylabel('$x(t)$')


plt.savefig("./../x_of_t_lin_exp.pdf", bbox_inches='tight')
plt.show()
