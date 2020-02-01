#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:54:25 2018

@author: obp48
"""
import numpy as np
import scipy
import matplotlib.pyplot as plt
from datetime import datetime



SCfigure=True
if SCfigure:
    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 15}
    plt.rc('font', **font)


T = 1000
dt=.1
sdt=np.sqrt(dt)
t=np.arange(0,(T)*dt,dt)

mu=.08
sigma=np.sqrt(.15)

noise=np.random.normal(loc=mu-sigma*sigma/2, scale=sigma*sdt, size=T)
logx=np.cumsum(noise)

#expectation value and time-average slopes
expectation=np.exp(mu*t)
t_growth_individual=np.exp((mu-sigma*sigma/2)*t)
t_growth_coop=np.exp((mu-sigma*sigma/4)*t)


#Plotting...
plt.plot(t,np.exp(logx),color='#0000FF',linewidth=2)


plt.plot([40,70],[np.exp(logx[int(40/dt)]),np.exp(logx[int(40/dt)])],color='k',linestyle='--',linewidth=2)
plt.plot([70,70],[np.exp(logx[int(40/dt)]),np.exp(logx[int(70/dt)])],color='k',linestyle='--',linewidth=2)
plt.annotate(s=r'$\delta t$',xy=(0.,20),xytext=(55,.5*np.exp(logx[int(40/dt)])))

#plt.annotate(s=r'$\Delta \ln x$',xy=(0.,20),xytext=(3.5+.1,wealth(3.5)-1.5*17))
#plt.plot([7.5,7.5],[wealth(5.5),wealth(7.5)],color='k',linestyle='--',linewidth=2)
#plt.plot([5.5,7.5],[wealth(5.5),wealth(5.5)],color='k',linestyle='--',linewidth=2)
#plt.annotate(s=r'$\Delta t$',xy=(0.,2),xytext=(5.5+.9,wealth(5.5)-1.5*17))
plt.annotate(s=r'$q$',xy=(0.,2),xytext=(73,2*np.exp(logx[int(40/dt)])))

#plt.annotate(s='',xy=(1.7,wealth(1.57)),xytext=(5.3,wealth(5.4)*.93),\
#             arrowprops=dict(facecolor='red',arrowstyle='<-',color='red'))


#plt.plot([2,2],[0,1.7])


#plt.plot(t,t_growth_individual,'g--', label=r'slope $\bar{g}(x_i)$')

#plt.plot(t,wealth_co,'b-',linewidth=3, label=r'$y^{(2)}(t)$')
#plt.plot(t,wealth_1,color='#00ff00',linewidth=3, label=r'$x_1(t)$')
#plt.plot(y,dist,color='#0000FF',linewidth=2, label=r'$x_1(t)$')


#low=.5
#high=.6
#plt.plot([low,low],[0,P(low)],color='r')         
#plt.plot([high,high],[0,P(high)],color='r')         
#py = y[np.logical_and(y >= low, y <= high)]
#plt.fill_between(
#        py,0,P(low),
##        P(py),
#        color='r',
#        alpha=0.3,
#        linewidth=0.1,
#    )

#plt.annotate(s='Dirac delta function\n of strength ' r'$\frac{N-1}{N}$',xy=(0.,.2),xytext=(.2,.6),\
#             arrowprops=dict(facecolor='black',arrowstyle='->'))

#plt.annotate(s='Dirac delta function\n of strength ' r'$\frac{1}{N}$',xy=(2.,.5),xytext=(.6,1.4),\
#            arrowprops=dict(facecolor='black',arrowstyle='->'))
         

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
#plt.gca().spines['bottom'].set_position('zero')

plt.yscale('log')
#plt.legend()
plt.xlabel('time $t$')
plt.ylabel('wealth $x$')
#plt.xlim([-.1,2.5])
#
#plt.xticks([0,2],\
#           [r'\$0',r'$\$100,000,000,000$'])
#            r'$10^{40}$'], rotation=0)
#plt.yticks([1,10.**10.,10.**20.,10.**30.,10.**40.],\
#           ['1',r'$10^{10}$',r'$10^{20}$',r'$10^{30}$',\
#            r'$10^{40}$'], rotation=0)

plt.savefig("./../gamble_process.pdf", bbox_inches='tight')
plt.show()