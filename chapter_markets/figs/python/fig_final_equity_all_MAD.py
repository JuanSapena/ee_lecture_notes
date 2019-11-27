#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:01:56 2018

@author: Ole Peters
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

#data_ID="BTC-USD"
#data_ID="STR-USD"
#data_ID="SP5-FED"
data_ID="STR-FET"
#data_ID="BTC-FED"
      
input_dir="./../../../../Leverage_Efficiency/data/"
#input_dir="./../../../../LML/Leverage_Efficiency/data/"
returns_1=pd.read_pickle(input_dir+data_ID+"-1.pkl")
returns_2=pd.read_pickle(input_dir+"BTC-FET"+"-1.pkl")
returns_3=pd.read_pickle(input_dir+"DAX-BNT"+"-1.pkl")
returns_4=pd.read_pickle(input_dir+"MAD-FTM"+"-1.pkl")
final_equity_1=np.cumprod(returns_1)[-1:].T
final_equity_2=np.cumprod(returns_2)[-1:].T
final_equity_3=np.cumprod(returns_3)[-1:].T
final_equity_4=np.cumprod(returns_4)[-1:].T
equity_1=np.cumprod(returns_1)
equity_2=np.cumprod(returns_2)
equity_3=np.cumprod(returns_3)
equity_4=np.cumprod(returns_4)

####final equity vs. leverage#####
fig, ax1=plt.subplots()
plt.axvline(x=1,linestyle=':',color='red',linewidth=1.5)
#plt.axvline(x=1+2*1.0403393028,linestyle=':',color='pink',linewidth=1.5)
#plt.axvline(x=1-2*1.0403393028,linestyle=':',color='pink',linewidth=1.5)
plt.axhline(y=0,linestyle=':',color='grey',linewidth=.5)
ax1.plot(final_equity_4, label='Madoff',linewidth=2,color='green')
ax1.plot(final_equity_1, label='S&P500TR',linewidth=2,color='blue')
ax1.plot(final_equity_3, label='DAX',linewidth=2,color='orange')
#ax2=ax1.twinx()
#ax2=ax1.twiny()
ax1.plot(final_equity_2, label='Bitcoin',linewidth=2,color='red')
ax1.set_yscale('log')
#ax2.set_yscale('log')
ax1.set_xlim([-35,105])
ax1.set_ylim([1e-23,1e20])
#ax2.set_ylim([0.1**5,10**7])
#plt.xlim([final_equity_1.index.min(),final_equity_1.index.max()])
#plt.ylim([-1.5,2.2])
#vals = ax.get_yticks()
#ax.set_yticklabels(['{:3.0f}% p.a.'.format(100*x) for x in vals])
#ax.set_aspect(1./(1.618*ax.get_data_ratio()))
#plt.title('some title')
ax1.set_xlabel('leverage')
ax1.set_ylabel('final equity')
#ax2.set_ylabel('final equity (BTC)',color='red')

#plt.axvline(x=1.68045,linestyle='--',color='grey',linewidth=1)
ax1.legend(loc=4, bbox_to_anchor=(.93,.5))
#ax2.legend(loc=4, bbox_to_anchor=(.38,.8))
#ax.legend_.remove()
plt.savefig("../all_MAD_final_equity.pdf", bbox_inches='tight')
plt.show()
