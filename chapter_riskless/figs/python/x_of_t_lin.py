#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:26:27 2020

@author: obp48
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:54:25 2018

@author: obp48
"""
import matplotlib.pyplot as plt
import numpy as np


SCfigure=True
if SCfigure:
    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 15}
    plt.rc('font', **font)

x0=2
gamma=17

#def v(eta,x):
#    v=(np.power(x,(1-eta))-1)/(1-eta)
#    return v

def wealth(t):
    wealth=x0+gamma*t
    return wealth


t=np.arange(0,8.,.01)
x=wealth(t)
    
#Plotting...
plt.plot(t,x,'b', label=r'')

plt.plot([1.5,3.5],[wealth(1.5),wealth(1.5)],color='k',linestyle='--',linewidth=2)
plt.plot([3.5,3.5],[wealth(1.5),wealth(3.5)],color='k',linestyle='--',linewidth=2)
plt.annotate(s=r'$\Delta t$',xy=(0.,.2),xytext=(1.5+1,wealth(1.5)-1*17))
plt.annotate(s=r'$\Delta x$',xy=(0.,.2),xytext=(3.5+.2,wealth(3.5)-1*17))

plt.plot([5.5,7.5],[wealth(5.5),wealth(5.5)],color='k',linestyle='--',linewidth=2)
plt.plot([7.5,7.5],[wealth(5.5),wealth(7.5)],color='k',linestyle='--',linewidth=2)
plt.annotate(s=r'$\Delta t$',xy=(0.,.2),xytext=(5.5+1,wealth(5.5)-1*17))
plt.annotate(s=r'$\Delta x$',xy=(0.,.2),xytext=(7.5+.2,wealth(7.5)-1*17))

plt.annotate(s='',xy=(5.5,wealth(5.5)-17*.3),xytext=(2,wealth(2)-17*.3),\
             arrowprops=dict(facecolor='black',arrowstyle='->',color='red'))


plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position('zero')

#plt.yscale('log')
#plt.legend()
plt.xlabel('time $t$')
plt.ylabel('wealth $x$')

plt.savefig("./../x_of_t_lin.pdf", bbox_inches='tight')
plt.show()