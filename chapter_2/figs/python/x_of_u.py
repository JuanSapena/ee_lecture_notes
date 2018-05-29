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
x=np.arange(-1.,2.,.01)

plt.plot(b_u*np.exp(x)+C,x,linestyle='-',color='blue')
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)
plt.xlabel('$u$',fontsize=16)
plt.ylabel('$x(u)$',fontsize=16)
plt.savefig("./../x_of_u.pdf", bbox_inches='tight')
plt.show()
