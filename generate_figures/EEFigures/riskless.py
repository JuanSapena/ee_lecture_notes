import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from . import base

def figure1(config):

    target_folder = config['figures folder']+config['riskless']['output folder']
    filename = '1_x_of_t_lin.pdf'
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

    # Add the line indicating wealth
    plt.plot(t,x, label="wealth")

    # Add lines indicating increments
    plt.plot([1.5,3.5],[wealth(1.5),wealth(1.5)],color='k',linestyle='--',linewidth=2)
    plt.plot([3.5,3.5],[wealth(1.5),wealth(3.5)],color='k',linestyle='--',linewidth=2)
    plt.plot([5.5,7.5],[wealth(5.5),wealth(5.5)],color='k',linestyle='--',linewidth=2)
    plt.plot([7.5,7.5],[wealth(5.5),wealth(7.5)],color='k',linestyle='--',linewidth=2)

    # Add text
    plt.annotate(s=r'$\Delta t$',xy=(0.,.2),xytext=(1.5+1,wealth(1.5)-1*17))
    plt.annotate(s=r'$\Delta x$',xy=(0.,.2),xytext=(3.5+.2,wealth(3.5)-1*17))
    plt.annotate(s=r'$\Delta t$',xy=(0.,.2),xytext=(5.5+1,wealth(5.5)-1*17))
    plt.annotate(s=r'$\Delta x$',xy=(0.,.2),xytext=(7.5+.2,wealth(7.5)-1*17))

    # Add arrow
    plt.annotate(s='',xy=(5.5,wealth(5.5)+17*.3),xytext=(2,wealth(2)+17*.3),\
                 arrowprops=dict(arrowstyle='->',color='red'))

    # Add axis labels
    plt.xlabel('time $t$')
    plt.ylabel('wealth $x$')

    # Apply final tweaks and save figure as pdf
    fig, ax =  base.apply_tweaks(config, fig, ax)
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
    # Try using custom tplot() functiont o transform the axes
    # First define the transformations to be applied to each axis
    def cx(x):
        return x

    def cy(x):
        return np.log10(x)

    #ax.plot(t,x, label=r'wealth')
    ax = base.tplot(t,x, cx, cy, ax, yticks='log')
    plt.plot([cx(1.5),cx(3.5)],[cy(wealth(1.5)),cy(wealth(1.5))],color='k',linestyle='--',linewidth=2)
    plt.plot([cx(3.5),cx(3.5)],[cy(wealth(1.5)),cy(wealth(3.5))],color='k',linestyle='--',linewidth=2)
    #plt.annotate(s=r'$\Delta t$',xy=(0.,20),xytext=(1.5+.9,wealth(1.5)-.5*17))
    #plt.annotate(s=r'$\Delta \ln x$',xy=(0.,20),xytext=(3.5+.1,wealth(3.5)-1.5*17))

    #plt.plot([5.5,7.5],[wealth(5.5),wealth(5.5)],color='k',linestyle='--',linewidth=2)
    #plt.plot([7.5,7.5],[wealth(5.5),wealth(7.5)],color='k',linestyle='--',linewidth=2)
    #plt.annotate(s=r'$\Delta t$',xy=(0.,2),xytext=(5.5+.9,wealth(5.5)-1.5*17))
    #plt.annotate(s=r'$\Delta \ln x$',xy=(0.,2),xytext=(7.5+.2,wealth(7.5)-1.8*17))

    #plt.annotate(s='',xy=(1.7,wealth(1.57)),xytext=(5.3,wealth(5.4)*.93),\
    #    arrowprops=dict(arrowstyle='<-',color='red'))

    ax.set_xlabel('time $t$')
    ax.set_ylabel('wealth $x$')
    #ax.set_yscale('log')
    fig, ax =  base.apply_tweaks(config, fig, ax)



#    plt.yscale('log')
#


    plt.savefig(target_folder+filename, bbox_inches='tight')
    return 0
