#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:06:55 2019

@author: Ole Peters
"""
import matplotlib.pyplot as plt
import numpy as np

mu=.05
sigma=np.sqrt(.2)
sigmaou=0
alpha=.1
N=5000
T = 10000
dt=.1
t=np.arange(0,(T+1)*dt,dt)
sdt=np.sqrt(dt)

#expectation value and time-average slopes
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
    v[tau]=v[tau-1]+sigma*noise[tau-1]*sdt+mu*dt

x=v**2

#Generate x
#noise=np.random.normal(loc=0, scale=sdt, size=(T,N))
#x=np.zeros((t.size,N))
#for tau in range(1,T+1):
#    x[tau]=x[tau-1]+np.sqrt(mu**2-sigma**2/t[tau])*dt+sigma*noise[tau-1]*sdt

#Plotting...
#plt.plot(expectation,t,color='#448832',label=r'slope $g(\langle x \rangle)$')
#plt.plot(t,t_growth_coop,'b--', label=r'slope $\bar{g}(y^{(2)})$')
#plt.plot(t,t_growth_individual,'g--', label=r'slope $\bar{g}(x_i)$')

#plt.plot(t,wealth_co,'b-',linewidth=3, label=r'$y^{(2)}(t)$')
#plt.plot(t,wealth_1,color='#00ff00',linewidth=3, label=r'$x_1(t)$')
#plt.plot(t,v,color='#000000',linewidth=1, label=r'$x_1(t)$')
#plt.plot(t,x,color='#0000ff',linewidth=1, label=r'$x_1(t)$')
#plt.plot(t,v.mean(1),color='#ff0000',linewidth=2, label=r'$x_1(t)$')
plt.plot(t,x.mean(1),color='#00ffff',linewidth=2, label=r'$x_1(t)$')
#plt.plot(t,np.sqrt(x.mean(1)),color='#00ff00',linewidth=2, label=r'$x_1(t)$')
         
#plt.plot(t,wealth_2,color='#55bb55',linewidth=3, label=r'$x_2(t)$')
#plt.plot(t,wealth_ave,'k-',linewidth=1, label=r'$(x_1(t)+x_2(t))/2$')

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
