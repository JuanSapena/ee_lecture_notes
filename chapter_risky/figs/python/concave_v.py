#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:56:34 2020

@author: obp48
"""

import matplotlib.pyplot as plt
import numpy as np

alpha=.125
mu=.05
sigma=np.sqrt(0.2)
N=10000
T = 500
dt=.1
t=np.arange(0,(T+1)*dt,dt)
sdt=np.sqrt(dt)

#generate Brownian motion
noise=np.random.normal(loc=0, scale=sdt, size=(T,N))
v=np.zeros((len(t),N))
v=v+10
for tau in range(1,len(t)):
    v[tau]=v[tau-1]+mu*dt+sigma*noise[tau-1]*sdt

#convert into x(t)=v^(-1)(BM)
x=(v**2)**(1./(2*alpha))

#plot zero-noise trajectory
plt.plot(t,((10+mu*t)**2)**(1./(2*alpha)),label=r"$x(t; \sigma=0)$",linewidth=3)

#average over many x(t)
#plot ensemble average
plt.plot(t,np.mean(x,1),label=r"$\langle x \rangle$")

#expectation value and time-average slopes
#wealth_det=mu*mu*t**2
#expectation=np.exp(mu*t)
#t_growth_individual=np.exp((mu-sigma*sigma/2)*t)
#t_growth_coop=np.exp((mu-sigma*sigma/4)*t)
#
##Generate wealth of individual 1
##noise_1=np.random.normal(loc=1+mu, scale=0, size=T)
##wealth_1=np.cumprod(noise_1)
##wealth_1=np.insert(wealth_1,0,1)
#
#
##Generate x
##noise=np.random.normal(loc=0, scale=sdt, size=(T,N))
##x=np.zeros((t.size,N))
##for tau in range(1,T+1):
##    x[tau]=x[tau-1]+np.sqrt(mu**2-sigma**2/t[tau])*dt+sigma*noise[tau-1]*sdt
#
##Plotting...
##plt.plot(t,x,color='#0000ff',linewidth=2, label=r'$x_1(t)$')
##plt.plot(t,x.mean(1),color='#00ff00',linewidth=2, label=r'$x_1(t)$')
#plt.plot(t,wealth_det**.5/t,color='#ff0000',linewidth=2, label=r'$x_1(t)$')
#plt.plot(t,x.mean(1)**.5/t,color='#00ff00',linewidth=2, label=r'$x_1(t)$')
#         

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

plt.title(r"$\alpha=$"+str(alpha))

#plt.yscale('log')
plt.legend()
plt.xlabel('time, $t$')
plt.ylabel('wealth')
#
#plt.yticks([1,10.**10.,10.**20.,10.**30.,10.**40.],\
#           ['1',r'$10^{10}$',r'$10^{20}$',r'$10^{30}$',\
#            r'$10^{40}$'], rotation=0)


plt.savefig("./../concave_v"+str(alpha)+".pdf", bbox_inches='tight')
plt.show()