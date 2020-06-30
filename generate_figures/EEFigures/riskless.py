import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from . import base

def figure1(config):

    target_folder = config['figures folder']+config['riskless']['output folder']
    filename = '1_x_of_t_lin.pdf'
    print("Plotting ", filename)

    x0=2
    gamma=17

    def wealth(t):
        wealth=x0+gamma*t
        return wealth


    t=np.arange(0,8.,.01)
    x=wealth(t)

    #Plotting...
    fig, ax = plt.subplots(1,1)
    for i in range(1,4):
        plt.plot(t,x + i*10, label="$i")

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

    plt.xlabel('time $t$')
    plt.ylabel('wealth $x$')

    plt.savefig(target_folder+filename, bbox_inches='tight')
    return 0

def figure2(config):
    target_folder = config['figures folder']+config['riskless']['output folder']
    filename = '2_ge_x_lin.pdf'
    print("Plotting ", filename)
    base.set_style(config)

    x0=2
    gamma=17

    def wealth(t):
        wealth=x0+gamma*t
        return wealth


    t=np.arange(0,8.,.01)
    x=wealth(t)

    #Plotting...
    fig, ax = plt.subplots(1,1)
    ax.plot(t,x, label=r'A')
    ax.plot(t,x+10, label=r'B')
    ax.plot(t,x+20, label=r'C')
    #plt.plot([1.5,3.5],[wealth(1.5),wealth(1.5)],color='k',linestyle='--',linewidth=2)
    #plt.plot([3.5,3.5],[wealth(1.5),wealth(3.5)],color='k',linestyle='--',linewidth=2)
    #plt.annotate(s=r'$\Delta t$',xy=(0.,20),xytext=(1.5+.9,wealth(1.5)-.5*17))
    #plt.annotate(s=r'$\Delta \ln x$',xy=(0.,20),xytext=(3.5+.1,wealth(3.5)-1.5*17))

    #plt.plot([5.5,7.5],[wealth(5.5),wealth(5.5)],color='k',linestyle='--',linewidth=2)
    #plt.plot([7.5,7.5],[wealth(5.5),wealth(7.5)],color='k',linestyle='--',linewidth=2)
    #plt.annotate(s=r'$\Delta t$',xy=(0.,2),xytext=(5.5+.9,wealth(5.5)-1.5*17))
    #plt.annotate(s=r'$\Delta \ln x$',xy=(0.,2),xytext=(7.5+.2,wealth(7.5)-1.8*17))

    #plt.annotate(s='',xy=(1.7,wealth(1.57)),xytext=(5.3,wealth(5.4)*.93),\
    #    arrowprops=dict(facecolor='red',arrowstyle='<-',color='red'))

    ax.set_xlabel('time $t$')
    ax.set_ylabel('wealth $x$')
    fig, ax =  base.apply_tweaks(config, fig, ax)



#    plt.yscale('log')
#


    plt.savefig(target_folder+filename, bbox_inches='tight')
    return 0
