# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
import math

SCfigure=True
if SCfigure:
    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 15}
    plt.rc('font', **font)

tau=.01
sigma=.18

#def v(eta,x):
#    v=(np.power(x,(1-eta))-1)/(1-eta)
#    return v

def P(y):
    zeta=1+2*tau/(sigma*sigma)
    P=(np.power((zeta-1),(zeta)))/math.gamma(zeta)*np.exp(-(zeta-1)/y)*np.power(y,-(1+zeta))
    return P

#def mag(eta):
#    mag=v(eta,300)+v(eta,130)-v(eta,220)-v(eta,190)
#    return mag

#eta=np.arange(.401,1.1,.01)
y=np.arange(.01,2.5,.01)
dist=P(y)
#zero=np.zeros(y.size)
#magnitude=np.zeros(y.size)

#position=0
#for x in y:
#    magnitude[position]=P(x)
#    position=position+1
    
#Plotting...
#plt.plot(expectation,t,color='#448832',label=r'slope $g(\langle x \rangle)$')
#plt.plot(t,t_growth_coop,'b--', label=r'slope $\bar{g}(y^{(2)})$')
#plt.plot(t,t_growth_individual,'g--', label=r'slope $\bar{g}(x_i)$')

#plt.plot(t,wealth_co,'b-',linewidth=3, label=r'$y^{(2)}(t)$')
#plt.plot(t,wealth_1,color='#00ff00',linewidth=3, label=r'$x_1(t)$')
plt.plot(y,dist,color='#0000FF',linewidth=2, label=r'$x_1(t)$')

low=.5
high=2.5
plt.plot([low,low],[0,P(low)],color='r')         
#plt.plot([high,high],[0,P(high)],color='r')         
py = y[np.logical_and(y >= low, y <= high)]
plt.fill_between(
        py,0,
        P(py),
        color='r',
        alpha=0.3,
        linewidth=0.1,
    )

plt.annotate(s=r'$x$',xy=(.5,0),xytext=(.8,.7),\
             arrowprops=dict(facecolor='black',arrowstyle='->'))

#plt.annotate(s=r'$x+\Delta x$',xy=(.6,0),xytext=(1,.5),\
#             arrowprops=dict(facecolor='black',arrowstyle='->'))
         
#plt.plot(eta,zero,color='#000000',linewidth=2, label=r'$x_1(t)$')
#plt.plot(t,wealth_2,color='#55bb55',linewidth=3, label=r'$x_2(t)$')
#plt.plot(t,wealth_ave,'k-',linewidth=1, label=r'$(x_1(t)+x_2(t))/2$')

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position('zero')

#plt.yscale('log')
#plt.legend()
plt.xlabel('wealth $x$')
plt.ylabel('wealth distribution $\mathcal{P}(x)$')
#plt.xlim([0,2])
#
plt.xticks([0,1,2],\
           [r'\$0',r'$\$100,000$',r'$\$200,000$'])
#            r'$10^{40}$'], rotation=0)
#plt.yticks([1,10.**10.,10.**20.,10.**30.,10.**40.],\
#           ['1',r'$10^{10}$',r'$10^{20}$',r'$10^{30}$',\
#            r'$10^{40}$'], rotation=0)


plt.savefig("./../wealth_dist_def_2.pdf", bbox_inches='tight')
plt.show()
