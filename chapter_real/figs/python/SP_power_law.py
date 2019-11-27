# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

output_dir="./../data/"

#1 1/2
#2 1/4
#4 1/8

N=31
tau=list(range(N))
#expectation=np.power(1.05,play_round)
#t_factor=np.sqrt(1.5*0.6)
#time_ave=np.power(t_factor,play_round)
#for n in range(0,N):
#    for t in range(0,T):
#        x[t,n]=x[t-1,n]*np.random.choice([0.6,1.5])
Dx=np.power(2,(tau))
p=.5*np.power(.5,(tau))

x=np.arange(.1,X,.001)
u=np.log(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


plt.plot(Dx,p,color='#0000ff',lineStyle='',marker='o')
#plt.plot([1.5,1.5],[0,np.log(1.5)],color='#7777ff',lineWidth=2,lineStyle=":")
#plt.plot([.6,.6],[0,np.log(.6)],color='#7777ff',lineWidth=2,lineStyle=":")
#plt.plot([1,1.5],[np.log(1.5),np.log(1.5)],color='#7777ff',lineWidth=2,lineStyle=":")
#plt.plot([.6,1],[np.log(.6),np.log(.6)],color='#7777ff',lineWidth=2,lineStyle=":")
##plt.plot([0, 1000],[1, 1], color='#555555',lineWidth=1)
##plt.plot([250, 250],[1, 5], color='#555555',lineWidth=1)
##plt.plot([500, 500],[1, 5], color='#555555',lineWidth=1)
##plt.plot([750, 750],[1, 5], color='#555555',lineWidth=1)
##plt.plot([1000, 1000],[1, 5], color='#555555',lineWidth=1)
#ax.annotate(r'$\langle \Delta x\rangle>0$', xy=(1.05,0), xytext=(1.2,-.3),
#            arrowprops=dict(shrink=0.05),backgroundcolor='white'
#            )
#ax.annotate(r'$\langle \Delta u\rangle<0$', xy=(1,(np.log(.6)+np.log(1.5))/2), xytext=(.75,-.4),
#            arrowprops=dict(shrink=0.05),backgroundcolor='white'
#            )
##ax.annotate('$500$', xy=(470,10), xytext=(470, 10))
##ax.annotate('$750$', xy=(720,10), xytext=(720, 10))
##ax.annotate('$1000$', xy=(950,10), xytext=(950, 10))
##
##plt.plot(expectation,color='b',lineWidth=2)
##plt.plot(time_ave,color='r',lineWidth=2)
#plt.xlim(.45,1.55)
#plt.ylim(-.55,.55)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$\Delta x$')
plt.ylabel(r'$p(\Delta x)$')
#
## Move left y-axis and bottom x-axis to centre, passing through (0,0)
#ax.spines['left'].set_position(('data',1))
##
## Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#ax.spines['bottom'].set_color('none')
#ax.spines['bottom'].set_position(('data',0))
##
### Show ticks in the left and lower axes only
##ax.yaxis.set_ticks_position('left')
#plt.xticks([.6,1.05,1.5],[r'$\Delta x_T$','',r'$\Delta x_H$'])
#plt.yticks([np.log(.6),(np.log(.6)+np.log(1.5))/2,np.log(1.5)],[r'$\Delta u_H$','',r'$\Delta u_T$'])
##plt.tick_params(
##    axis='x',          # changes apply to the x-axis
##    which='both',      # both major and minor ticks are affected
##    bottom=False,      # ticks along the bottom edge are off
##    top=False,         # ticks along the top edge are off
##    labelbottom=False) # labels along the bottom edge are off
##
###plt.axis('off')
plt.savefig("./../figs/St_Petersburg.pdf", bbox_inches='tight')
#
