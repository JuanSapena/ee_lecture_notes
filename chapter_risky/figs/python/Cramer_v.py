#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:06:55 2019

@author: Ole Peters
"""
import matplotlib.pyplot as plt
import numpy as np

mu=.05
sigma=np.sqrt(1)
N=500
T = 10000
dt=.1
t=np.arange(0,(T+1)*dt,dt)
sdt=np.sqrt(dt)

#expectation value and time-average slopes
wealth_det=mu*mu*t**2
expectation=np.exp(mu*t)
t_growth_individual=np.exp((mu-sigma*sigma/2)*t)
t_growth_coop=np.exp((mu-sigma*sigma/4)*t)

#Generate wealth of individual 1
#noise_1=np.random.normal(loc=1+mu, scale=0, size=T)
#wealth_1=np.cumprod(noise_1)
#wealth_1=np.insert(wealth_1,0,1)

#Generate v(t)
noise=np.random.normal(loc=0, scale=sdt, size=(T,N))
v=np.zeros((t.size,N))
for tau in range(1,T+1):
    v[tau]=v[tau-1]+mu*dt+sigma*noise[tau-1]*sdt

x=v**2

#Generate x
#noise=np.random.normal(loc=0, scale=sdt, size=(T,N))
#x=np.zeros((t.size,N))
#for tau in range(1,T+1):
#    x[tau]=x[tau-1]+np.sqrt(mu**2-sigma**2/t[tau])*dt+sigma*noise[tau-1]*sdt

#Plotting...
#plt.plot(t,x,color='#0000ff',linewidth=2, label=r'$x_1(t)$')
#plt.plot(t,x.mean(1),color='#00ff00',linewidth=2, label=r'$x_1(t)$')
plt.plot(t,wealth_det**.5/t,color='#ff0000',linewidth=2, label=r'$x_1(t)$')
plt.plot(t,x.mean(1)**.5/t,color='#00ff00',linewidth=2, label=r'$x_1(t)$')
         

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

#plt.yscale('log')
#plt.legend()
plt.xlabel('time, $t$')
plt.ylabel('wealth')
#
#plt.yticks([1,10.**10.,10.**20.,10.**30.,10.**40.],\
#           ['1',r'$10^{10}$',r'$10^{20}$',r'$10^{30}$',\
#            r'$10^{40}$'], rotation=0)


#plt.savefig("./../cramer_v.pdf", bbox_inches='tight')
plt.show()
