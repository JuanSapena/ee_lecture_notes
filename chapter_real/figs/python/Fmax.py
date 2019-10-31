#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:06:55 2019

@author: Ole Peters
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

def v(eta,x):
    v=(np.power(x,(1-eta))-1)/(1-eta)
    return v

def mag(eta):
    mag=v(eta,300)+v(eta,130)-v(eta,220)-v(eta,190)
    return mag

def ave_g(F,x):
    g=0
    p=.5
    q=1
    for j in range(100):
       g=g+p*np.log((x+q-F)/x) 
       q=q*2
       p=p*.5
    return g

data_points=220
wealth=np.zeros(data_points)
Fmax=np.zeros(data_points)
x=.1
for i in range(data_points):
    wealth[i]=x
    Fmax[i]=optimize.root_scalar(ave_g, x0=0, args=(x), bracket=[0, 100],method='bisect').root
    x=x*1.1
    
    
#Plotting...
#plt.plot(expectation,t,color='#448832',label=r'slope $g(\langle x \rangle)$')
#plt.plot(t,t_growth_coop,'b--', label=r'slope $\bar{g}(y^{(2)})$')
#plt.plot(t,t_growth_individual,'g--', label=r'slope $\bar{g}(x_i)$')

#plt.plot(t,wealth_co,'b-',linewidth=3, label=r'$y^{(2)}(t)$')
#plt.plot(t,wealth_1,color='#00ff00',linewidth=3, label=r'$x_1(t)$')
plt.plot(wealth,Fmax,color='#0000FF',linewidth=2, label=r'$x_1(t)$')
#plt.plot(eta,zero,color='#000000',linewidth=2, label=r'$x_1(t)$')
#plt.plot(t,wealth_2,color='#55bb55',linewidth=3, label=r'$x_2(t)$')
#plt.plot(t,wealth_ave,'k-',linewidth=1, label=r'$(x_1(t)+x_2(t))/2$')

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

plt.xscale('log')
#plt.legend()
plt.xlabel('wealth $x$')
plt.ylabel('maximum fee $F^{\text{max}}$')
#
#plt.yticks([1,10.**10.,10.**20.,10.**30.,10.**40.],\
#           ['1',r'$10^{10}$',r'$10^{20}$',r'$10^{30}$',\
#            r'$10^{40}$'], rotation=0)


plt.savefig("./../Fmax.pdf", bbox_inches='tight')
plt.show()
