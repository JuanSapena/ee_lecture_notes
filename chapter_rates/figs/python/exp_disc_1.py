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


b_u=1
C=1
x=np.arange(-.1,2.,.01)

plt.semilogy([1, 1], [1, 11], 'r-', lw=3)
plt.semilogy([2, 2], [1, 26], 'b-', lw=3)
plt.semilogy([0, 1], [1, 11], 'r:', lw=3)
plt.semilogy([0, 2], [1, 26], 'b:', lw=3)
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
#plt.xlabel('$t$',fontsize=16)
#plt.ylabel('Payment',fontsize=16)
plt.xticks([0,1,2], ['1 Jul','1 Aug','1 Sep'], rotation=0)
plt.yticks([1,10], ['$1','$10','$100'], rotation=0)
plt.savefig("./../exp_disc_1.pdf", bbox_inches='tight')
plt.show()
