#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:54:25 2018

@author: obp48
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

T=100
N=5
m=1.

noise=pd.DataFrame(np.random.normal(0,1,size=[N,T+1]),index=range(1,N+1))
x=pd.DataFrame(index=range(1,N+1),columns=range(0,T+1))
x.iloc[:,0]=np.random.normal(0,1,size=N)

for t in range(1,T+1):
    x.iloc[:,t]=x.iloc[:,t-1]*(1-m)+noise.iloc[:,t-1]

fig=plt.figure()

ax=x.iloc[1,:].plot(linestyle='-',color='blue')
plt.plot(range(0,T+1),x.iloc[2,:]-10,linestyle='-',color='blue')
plt.plot(range(0,T+1),x.iloc[3,:]-20,linestyle='-',color='blue')
plt.plot(range(0,T+1),x.iloc[4,:]-30,linestyle='-',color='blue')
plt.plot(range(0,T+1),x.iloc[0,:]-40,linestyle='-',color='blue')

plt.ylim([-55,20])
plt.xlim([-5,110])
plt.axis('off')

ax.annotate('',\
            xy=(105,8), xycoords='data',\
            xytext=(-310, 0), textcoords='offset points',\
            arrowprops=dict(color='green',arrowstyle="->",linewidth=2))
ax.annotate('',\
            xy=(110,-20), xycoords='data',\
            xytext=(-310, 0), textcoords='offset points',\
            arrowprops=dict(color='green',arrowstyle="->",linewidth=2,linestyle='--'))
ax.annotate('',\
            xy=(-5,-50), xycoords='data',\
            xytext=(0, 160), textcoords='offset points',\
            arrowprops=dict(color='red',arrowstyle="->",linewidth=2))
ax.annotate('',\
            xy=(45,-55), xycoords='data',\
            xytext=(0, 180), textcoords='offset points',\
            arrowprops=dict(color='red',arrowstyle="->",linewidth=2,linestyle='--'))
#plt.rc('xtick',labelsize=16)
#plt.rc('ytick',labelsize=16)
plt.xlabel('r$t$',fontsize=16)
#plt.ylabel('$u(x)$',fontsize=16)
plt.savefig("./../ergodic_grid.pdf", bbox_inches='tight')
#plt.show()
