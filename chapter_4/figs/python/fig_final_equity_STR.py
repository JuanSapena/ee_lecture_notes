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
      
input_dir="./../../../../LML/Leverage_Efficiency/data/"
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
#fig=plt.figure()
#ax=
plt.axvline(x=1,linestyle=':',color='red',linewidth=1.5)
plt.axvline(x=1+2*1.0403393028,linestyle=':',color='pink',linewidth=1.5)
plt.axvline(x=1-2*1.0403393028,linestyle=':',color='pink',linewidth=1.5)
plt.axhline(y=0,linestyle=':',color='grey',linewidth=.5)
plt.plot(final_equity_1,linewidth=2)
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
