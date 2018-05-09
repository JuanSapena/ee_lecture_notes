#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:55:07 2018

@author: obp48
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
      
input_dir="./../../../../LML/Leverage_Efficiency/data/"
returns=pd.read_pickle(input_dir+"STR-FED-1.pkl")
equity=np.cumprod(returns)
final_equity=equity[-1:].T

#### equity trajectories ####
fig=plt.figure()

Delta_t=returns.index[-1] - returns.index[0]
years=Delta_t.days/365.25
#ax=(np.log(final_equity.iloc[:,0].astype(float))/years).plot()
ax=equity.iloc[:,244].plot(label='l='+str(round(equity.columns[244],2)))
equity.iloc[:,270].plot(label='l='+str(round(equity.columns[270],2)))
equity.iloc[:,372].plot(label='l='+str(round(equity.columns[372],2)))
#equity.iloc[:,451].plot(label='l='+str(round(equity.columns[451],2)))
#equity.iloc[:,470].plot(label='l='+str(round(equity.columns[470],2)))
ax.set_yscale('log')
#plt.xlim([final_equity.index.min(),final_equity.index.max()])
plt.ylim([10**-3,10**3])
#vals = ax.get_yticks()
#ax.set_yticklabels(['{:3.0f}% p.a.'.format(100*x) for x in vals])
#ax.set_aspect(1./(1.618*ax.get_data_ratio()))
#plt.title('some title')
plt.xlabel('')
plt.ylabel('equity')
#plt.axvline(x=0,linestyle=':',color='grey',linewidth=.5)
plt.axhline(y=1,linestyle=':',color='black',linewidth=.5)
#plt.axvline(x=1.68045,linestyle='--',color='grey',linewidth=1)
plt.legend(loc=1, bbox_to_anchor=(.35,.35))
#ax.legend_.remove()
plt.savefig("../STR-FED-1_equity.pdf", bbox_inches='tight')
plt.show()
