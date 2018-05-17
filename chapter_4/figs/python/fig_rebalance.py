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
#data_ID="STR-FED"
#data_ID="BTC-FED"
      
#input_dir="./../../../../Leverage_Efficiency/data/"
#returns_1=pd.read_pickle(input_dir+"STR-FED"+"-1.pkl")
#returns_2=pd.read_pickle(input_dir+"BTC-FED"+"-1.pkl")
#returns_3=pd.read_pickle(input_dir+"DAX-BND"+"-1.pkl")
#final_equity_1=np.cumprod(returns_1)[-1:].T
#final_equity_2=np.cumprod(returns_2)[-1:].T
#final_equity_3=np.cumprod(returns_3)[-1:].T
#equity_1=np.cumprod(returns_1)
#equity_2=np.cumprod(returns_2)
#equity_3=np.cumprod(returns_3)

####final equity vs. leverage#####
fig, ax1=plt.subplots()
#plt.axvline(x=1,linestyle=':',color='black',linewidth=1.5)
ax1.fill_betweenx([0,3],-1,-.8,color=(1,0,0,1))
ax1.fill_betweenx([0,7],-.6,-.4,color=(0,0,1,1))
#l=.7
ax1.annotate('l=0.7', xy=(6, 9), xytext=(-1,13))
ax1.annotate('apply returns', xy=(6, 1), xytext=(0.3,6))
ax1.annotate('', xy=(2.5,8), xytext=(0,8),arrowprops=dict(facecolor='black', shrink=0.05))

ax1.fill_betweenx([0,3.3],3,3.2,color=(1,0,0,1),label='risky')
ax1.fill_betweenx([0,12],3.4,3.6,color=(0,0,1,1),label='riskless')
#l=12/15.3
ax1.annotate('l=0.78', xy=(6, 9), xytext=(3,13))
ax1.annotate('re-balance', xy=(4,6), xytext=(3.7,6)
            )
ax1.annotate('', xy=(5.3,8), xytext=(3.7,8),arrowprops=dict(facecolor='black', shrink=0.05))

ax1.annotate('l=0.7', xy=(6, 9), xytext=(5,13))
ax1.fill_betweenx([0,.3*15.3],5,5.2,color=(1,0,0,1))
ax1.fill_betweenx([0,.7*15.3],5.4,5.6,color=(0,0,1,1))
#l=.7


plt.axhline(y=0,linestyle=':',color='grey',linewidth=.5)
#ax1.plot(final_equity_1, label='S&P500TR',linewidth=2,color='blue')
#ax1.plot(final_equity_3, label='DAX',linewidth=2,color='orange')
#ax2=ax1.twinx()
#ax2.plot(final_equity_2, label='Bitcoin',linewidth=2,color='red')
#ax1.set_yscale('log')
#ax2.set_yscale('log')
ax1.set_xlim([-2,7])
ax1.set_ylim([0,15])
#ax2.set_ylim([0.1**5,10**7])
#plt.xlim([final_equity_1.index.min(),final_equity_1.index.max()])
#plt.ylim([-1.5,2.2])
#vals = ax.get_yticks()
#ax.set_yticklabels(['{:3.0f}% p.a.'.format(100*x) for x in vals])
#ax.set_aspect(1./(1.618*ax.get_data_ratio()))
#plt.title('some title')
#ax1.set_xlabel('day')
#ax1.set_ylabel('holding')
#ax2.set_ylabel('final equity (BTC)',color='red')
plt.tick_params(\
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off',
    right='off',
    left='off',
    labelleft='off'
    )
#plt.axvline(x=1.68045,linestyle='--',color='grey',linewidth=1)
#ax1.legend(loc=4, bbox_to_anchor=(.93,.5))
#ax1.legend(loc=4, bbox_to_anchor=(.38,.8))
#ax.legend_.remove()
plt.savefig("../rebalance.pdf", bbox_inches='tight')
plt.show()
