#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:06:55 2019

@author: Ole Peters
"""
import matplotlib.pyplot as plt
import numpy as np

mu=.03
sigma=np.sqrt(.2)
sigmaou=1
alpha=.1
T = 1000
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

#Generate OU
noise_2=np.random.normal(loc=0, scale=sigma*sdt, size=T)
ou=np.zeros(t.size)
for tau in range(1,T+1):
    ou[tau]=ou[tau-1]-alpha*ou[tau-1]+sigmaou*noise_2[tau-1]*sdt

noisy_x=expectation+ou
#Generate wealth of individual 2
#noise_2=np.random.normal(loc=1+mu*dt, scale=sigma*sdt, size=T)
#wealth_2=np.cumprod(noise_2)
#wealth_2=np.insert(wealth_2,0,1)

#Generate average wealth of individuals
#wealth_ave=(wealth_1+wealth_2)/2

#Generate wealth of cooperating individuals
#noise_co=(noise_1+noise_2)/2
#wealth_co=np.cumprod(noise_co)
#wealth_co=np.insert(wealth_co,0,1)

#Plotting...
#plt.plot(expectation,t,color='#448832',label=r'slope $g(\langle x \rangle)$')
#plt.plot(t,t_growth_coop,'b--', label=r'slope $\bar{g}(y^{(2)})$')
#plt.plot(t,t_growth_individual,'g--', label=r'slope $\bar{g}(x_i)$')

#plt.plot(t,wealth_co,'b-',linewidth=3, label=r'$y^{(2)}(t)$')
#plt.plot(t,wealth_1,color='#00ff00',linewidth=3, label=r'$x_1(t)$')
plt.plot(t,noisy_x,color='#000000',linewidth=2, label=r'$x_1(t)$')
#plt.plot(t,wealth_2,color='#55bb55',linewidth=3, label=r'$x_2(t)$')
#plt.plot(t,wealth_ave,'k-',linewidth=1, label=r'$(x_1(t)+x_2(t))/2$')

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

plt.yscale('log')
#plt.legend()
plt.xlabel('time, $t$')
plt.ylabel('wealth')
#
#plt.yticks([1,10.**10.,10.**20.,10.**30.,10.**40.],\
#           ['1',r'$10^{10}$',r'$10^{20}$',r'$10^{30}$',\
#            r'$10^{40}$'], rotation=0)


#plt.savefig("./../add_noise_exp_growth_b.pdf", bbox_inches='tight')
plt.show()
