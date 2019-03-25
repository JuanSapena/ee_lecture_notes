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

plt.plot([1, 1], [0, 1], 'k-', lw=3)
plt.plot([2, 2], [0, 3], 'k-', lw=3)
plt.plot([0.75, 2], [0, 3], 'r:', lw=4)
plt.plot([0.75, 1], [0, 1], 'b:', lw=3)
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.xticks([0,1,2], ['1 Jul','1 Aug','1 Sep'], rotation=0)
plt.yticks([0,1,2,3], ['','$1','$2','$3'], rotation=0)
plt.savefig("./../disc_3.pdf", bbox_inches='tight')
plt.show()
