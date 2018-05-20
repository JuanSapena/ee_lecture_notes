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
data_ID="STR-FED"
#data_ID="BTC-FED"
      
input_dir="./../../../../Leverage_Efficiency/data/"
returns_1=pd.read_pickle(input_dir+data_ID+"-1.pkl")
returns_2=pd.read_pickle(input_dir+data_ID+"-2.pkl")
returns_3=pd.read_pickle(input_dir+data_ID+"-3.pkl")
final_equity_1=np.cumprod(returns_1)[-1:].T
final_equity_2=np.cumprod(returns_2)[-1:].T
final_equity_3=np.cumprod(returns_3)[-1:].T
equity_1=np.cumprod(returns_1)
equity_2=np.cumprod(returns_2)
equity_3=np.cumprod(returns_3)


####final equity vs. leverage#####
fig=plt.figure()
ax=final_equity_1.plot(linewidth=2,color='blue')
plt.plot(final_equity_1.index[219],final_equity_1.iloc[219],marker='o',markerfacecolor='none',linewidth=.1,color='brown')
plt.plot(final_equity_1.index[244],final_equity_1.iloc[244],marker='o',markerfacecolor='none',linewidth=.1,color='red')
plt.plot(final_equity_1.index[270],final_equity_1.iloc[270],marker='o',markerfacecolor='none',linewidth=.1,color='green')
plt.plot(final_equity_1.index[295],final_equity_1.iloc[295],marker='o',markerfacecolor='none',linewidth=.1,color='magenta')
plt.plot(final_equity_1.index[321],final_equity_1.iloc[321],marker='o',markerfacecolor='none',linewidth=.1,color='orange')
plt.plot(final_equity_1.index[346],final_equity_1.iloc[346],marker='o',markerfacecolor='none',linewidth=.1,color='purple')
plt.axvline(x=1,linestyle=':',color='red',linewidth=1.5)
plt.axvline(x=1+2*1.0403393028,linestyle=':',color='pink',linewidth=1.5)
plt.axvline(x=1-2*1.0403393028,linestyle=':',color='pink',linewidth=1.5)
plt.axhline(y=0,linestyle=':',color='grey',linewidth=.5)


ax.annotate('l=0',
            xy=(0,final_equity_1.iloc[219]), xycoords='data',
            xytext=(-40, 0), textcoords='offset points',
            arrowprops=dict(color='brown',arrowstyle="->"))

ax.annotate('l=1',
            xy=(1,final_equity_1.iloc[244]), xycoords='data',
            xytext=(40, 0), textcoords='offset points',
            arrowprops=dict(color='red',arrowstyle="->"))

ax.annotate('l=2',
            xy=(2,final_equity_1.iloc[270]), xycoords='data',
            xytext=(30, -20), textcoords='offset points',
            arrowprops=dict(color='green',arrowstyle="->"))

ax.annotate('l=3',
            xy=(3,final_equity_1.iloc[295]), xycoords='data',
            xytext=(40, 0), textcoords='offset points',
            arrowprops=dict(color='magenta',arrowstyle="->"))

ax.annotate('l=4',
            xy=(4,final_equity_1.iloc[321]), xycoords='data',
            xytext=(40, 0), textcoords='offset points',
            arrowprops=dict(color='orange',arrowstyle="->"))

ax.annotate('l=5',
            xy=(5,final_equity_1.iloc[346]), xycoords='data',
            xytext=(-50, 0), textcoords='offset points',
            arrowprops=dict(color='purple',arrowstyle="->"))


#plt.plot(final_equity_2, label='+ friction',linewidth=3)
#plt.plot(final_equity_3, label='+ borrowing premia',linewidth=1)
#ax.set_yscale('log')
plt.xlim([-2,6])
#plt.xlim([final_equity_1.index.min(),final_equity_1.index.max()])
#plt.ylim([-1.5,2.2])
#vals = ax.get_yticks()
#ax.set_yticklabels(['{:3.0f}% p.a.'.format(100*x) for x in vals])
#ax.set_aspect(1./(1.618*ax.get_data_ratio()))
#plt.title('some title')
plt.xlabel('leverage')
plt.ylabel('final equity')

#plt.axvline(x=1.68045,linestyle='--',color='grey',linewidth=1)
#plt.legend(loc=4, bbox_to_anchor=(.45,.7))
#ax.legend_.remove()
plt.savefig("../"+data_ID+"_final_equity.pdf", bbox_inches='tight')
plt.show()
