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


m1=.5
s1=.3

m2=.6
s2=.7
x=np.arange(-1.,2.,.01)

plt.plot(x,1/(np.sqrt(2*s1**2)*np.exp((x-m1)**2/(2*s1**2))),linestyle='-',linewidth=3,color='blue')
plt.plot(x,1/(np.sqrt(2*s2**2)*np.exp((x-m2)**2/(2*s2**2))),linestyle='-',linewidth=3,color='red')
plt.xlabel(r'$r=\frac{\delta x}{\delta t}$')
plt.ylabel(r'$\mathcal{P}(r)$')
plt.xlim([-1,2])
plt.savefig("./../two_dists.pdf", bbox_inches='tight')
plt.show()
