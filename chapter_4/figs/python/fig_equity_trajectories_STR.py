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
      
input_dir="./../../../../Leverage_Efficiency/data/"
returns=pd.read_pickle(input_dir+"STR-FED-1.pkl")
equity=np.cumprod(returns)
final_equity=equity[-1:].T

#### equity trajectories ####
fig=plt.figure()

Delta_t=returns.index[-1] - returns.index[0]
years=Delta_t.days/365.25
#ax=(np.log(final_equity.iloc[:,0].astype(float))/years).plot()
ax=equity.iloc[:,219].plot(label='l='+str(round(int(equity.columns[219]))),color='brown')
equity.iloc[:,244].plot(label='l='+str(int(round(equity.columns[244],1))),color='red')
equity.iloc[:,270].plot(label='l='+str(int(round(equity.columns[270]))),color='green')
equity.iloc[:,295].plot(label='l='+str(int(round(equity.columns[295]))),color='magenta')
equity.iloc[:,321].plot(label='l='+str(int(round(equity.columns[321]))),color='orange')
equity.iloc[:,346].plot(label='l='+str(int(round(equity.columns[346]))),color='purple')
#equity.iloc[:,451].plot(label='l='+str(round(equity.columns[451],2)))
#equity.iloc[:,470].plot(label='l='+str(round(equity.columns[470],2)))
#ax.set_yscale('log')
ax.annotate('l=0',
            xy=(equity.index[-1],equity.iloc[-1,219]), xycoords='data',
            xytext=(40, 0), textcoords='offset points',
            arrowprops=dict(color='brown',arrowstyle="->"))

ax.annotate('l=1',
            xy=(equity.index[-1],equity.iloc[-1,244]), xycoords='data',
            xytext=(40, 0), textcoords='offset points',
            arrowprops=dict(color='red',arrowstyle="->"))

ax.annotate('l=2',
            xy=(equity.index[-1],equity.iloc[-1,270]), xycoords='data',
            xytext=(40, 0), textcoords='offset points',
            arrowprops=dict(color='green',arrowstyle="->"))

ax.annotate('l=3',
            xy=(equity.index[-1],equity.iloc[-1,295]), xycoords='data',
            xytext=(40, 0), textcoords='offset points',
            arrowprops=dict(color='magenta',arrowstyle="->"))

ax.annotate('l=4',
            xy=(equity.index[-1],equity.iloc[-1,321]), xycoords='data',
            xytext=(40, 0), textcoords='offset points',
            arrowprops=dict(color='orange',arrowstyle="->"))

ax.annotate('l=5',
            xy=(equity.index[-1],equity.iloc[-1,346]), xycoords='data',
            xytext=(40, 10), textcoords='offset points',
            arrowprops=dict(color='purple',arrowstyle="->"))


plt.xlim([equity.index[0],equity.index[-1]])
plt.ylim([0,100])
#vals = ax.get_yticks()
#ax.set_yticklabels(['{:3.0f}% p.a.'.format(100*x) for x in vals])
#ax.set_aspect(1./(1.618*ax.get_data_ratio()))
#plt.title('some title')
plt.xlabel('')
plt.ylabel('equity')
#plt.axvline(x=0,linestyle=':',color='grey',linewidth=.5)
plt.axhline(y=1,linestyle=':',color='black',linewidth=.5)
#plt.axvline(x=1.68045,linestyle='--',color='grey',linewidth=1)
#plt.legend(loc=1, bbox_to_anchor=(.75,.85))
#ax.legend_.remove()
plt.savefig("../STR-FED-1_equity.pdf", bbox_inches='tight')
plt.show()
