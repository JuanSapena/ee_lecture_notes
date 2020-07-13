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

    ax = base.tplot(t,x, cx, cy, ax, yticks='log')
    plt.plot([cx(1.5),cx(3.5)],[cy(wealth(1.5)),cy(wealth(1.5))],color='k',linestyle='--',linewidth=2)
    plt.plot([cx(3.5),cx(3.5)],[cy(wealth(1.5)),cy(wealth(3.5))],color='k',linestyle='--',linewidth=2)
    plt.annotate(s=r'$\Delta t$',xy=(cx(0.0),cy(20)),xytext=(cx(1.5+.9),cy(wealth(1.5)-.5*17)))
    plt.annotate(s=r'$\Delta \ln x$',xy=(cx(0.0),cy(20)),xytext=(cx(3.5+.1),cy(wealth(3.5)-1.5*17)))

    plt.plot([cx(5.5),cx(7.5)],[cy(wealth(5.5)),cy(wealth(5.5))],color='k',linestyle='--',linewidth=2)
    plt.plot([cx(7.5),cx(7.5)],[cy(wealth(5.5)),cy(wealth(7.5))],color='k',linestyle='--',linewidth=2)
    plt.annotate(s=r'$\Delta t$',xy=(cx(0.),cy(2)),xytext=(cx(5.5+.9),cy(wealth(5.5)-1.5*17)))
    plt.annotate(s=r'$\Delta \ln x$',xy=(cx(0.),cy(2)),xytext=(cx(7.5+.2),cy(wealth(7.5)-1.8*17)))

    plt.annotate(s='',xy=(cx(1.7),cy(wealth(1.57))),xytext=(cx(5.3),cy(wealth(5.4)*.93)),\
        arrowprops=dict(arrowstyle='<-',color='red'))

    ax.set_xlabel('time $t$')
    ax.set_ylabel('wealth $x$')
    ax.set_ylim([cy(1.0), cy(200.0)])
    fig, ax =  base.apply_tweaks(config, fig, ax)


    plt.savefig(target_folder+filename, bbox_inches='tight')
    return 0

def figure3(config):
    target_folder = config['figures folder']+config['riskless']['output folder']
    base.set_style(config)

    filename = 'disc_1.pdf'
    print("Plotting chapter 3, figure 3", filename)

    #Create plot
    fig, ax = plt.subplots(1,1)
    base.set_style(config)

    # Plot the lines
    ax.plot([1, 1], [0, 10], 'k-', lw=3)
    ax.plot([2, 2], [0, 25], 'k-', lw=3)
    ax.plot([0, 2], [0, 25], ':', lw=4)
    ax.plot([0, 1], [0, 10], ':', lw=3)

    # Customise the axis ticks
    ax.set_xticks([0,1,2])
    ax.set_xticklabels(['1 Jul','1 Aug','1 Sep'], rotation=0)
    ax.set_yticks([0,10,20,30])
    ax.set_yticklabels(['','$10','$20','$30'], rotation=0)

    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    filename = 'disc_2.pdf'
    print("Plotting chapter 3, figure 3", filename)
    #Create plot
    fig, ax = plt.subplots(1,1)
    base.set_style(config)

    # Plot the lines
    ax.plot([1, 1], [0, 10], 'k-', lw=3)
    ax.plot([2, 2], [0, 25], 'k-', lw=3)
    ax.plot([1./3, 2], [0, 25], ':', lw=4)
    ax.plot([1./3, 1], [0, 10], ':', lw=3)

    # Customise the axis ticks
    ax.set_xticks([0,1,2])
    ax.set_xticklabels(['1 Jul','1 Aug','1 Sep'], rotation=0)
    ax.set_yticks([0,10,20,30])
    ax.set_yticklabels(['','$10','$20','$30'], rotation=0)

    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')


    filename = 'disc_3.pdf'
    print("Plotting chapter 3, figure 3", filename)
    #Create plot
    fig, ax = plt.subplots(1,1)
    base.set_style(config)

    # Plot the lines
    ax.plot([1, 1], [0, 10], 'k-', lw=3)
    ax.plot([2, 2], [0, 25], 'k-', lw=3)
    ax.plot([2./3, 2], [0, 25], ':', lw=4)
    ax.plot([2./3, 1], [0, 10], ':', lw=3)

    # Customise the axis ticks
    ax.set_xticks([0,1,2])
    ax.set_xticklabels(['1 Jul','1 Aug','1 Sep'], rotation=0)
    ax.set_yticks([0,10,20,30])
    ax.set_yticklabels(['','$10','$20','$30'], rotation=0)

    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    return 0

def figure4(config):
    target_folder = config['figures folder']+config['riskless']['output folder']
    base.set_style(config)
    # Get the list of default line colors
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # We will use the custom tplot() function to transform the axes to semilog.
    # First define the transformations to be applied to each axis
    def cx(x):
        return x

    def cy(x):
        return np.log10(x)

    #Create first sub-figure
    filename = 'exp_disc_1.pdf'
    print("Plotting chapter 3, figure 4", filename)
    fig, ax = plt.subplots(1,1)

    # Add the lines to the plot
    ax = base.tplot([1, 1], [1, 11], cx, cy, ax, yticks='log', label = 'L1')
    ax = base.tplot([2, 2], [1, 26], cx, cy, ax, yticks='log', label = 'L2')
    ax = base.tplot([0, 1], [1, 11], cx, cy, ax, yticks='log', label = 'L3')
    ax = base.tplot([0, 2], [1, 26], cx, cy, ax, yticks='log', label = 'L4')
    # Tweak the properties of the lines
    L = ax.lines
    for line in L:
        line.set_linewidth(3)
    L[0].set_color(colors[0])
    L[1].set_color(colors[1])
    L[2].set_color(colors[0])
    L[2].set_linestyle(':')
    L[3].set_color(colors[1])
    L[3].set_linestyle(':')

    # Customise the axis ticks
    ax.set_xticks([cx(0),cx(1),cx(2)])
    ax.set_xticklabels(['1 Jul','1 Aug','1 Sep'], rotation=0)
    ax.set_yticks([cy(1), cy(10), cy(100)])
    ax.set_yticklabels(['$1','$10','$100'], rotation=0)

    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    # Create  second sub-plot
    filename = 'exp_disc_2.pdf'
    print("Plotting chapter 3, figure 4", filename)

    fig, ax = plt.subplots(1,1)


    # Add the lines to the plot
    ax = base.tplot([1, 1], [100, 110], cx, cy, ax, yticks='log', label = 'L1')
    ax = base.tplot([2, 2], [100, 125], cx, cy, ax, yticks='log', label = 'L2')
    ax = base.tplot([0, 1], [100, 110], cx, cy, ax, yticks='log', label = 'L3')
    ax = base.tplot([0, 2], [100, 125], cx, cy, ax, yticks='log', label = 'L4')
    # Tweak the properties of the lines
    L = ax.lines
    for line in L:
        line.set_linewidth(3)
    L[0].set_color(colors[0])
    L[1].set_color(colors[1])
    L[2].set_color(colors[0])
    L[2].set_linestyle(':')
    L[3].set_color(colors[1])
    L[3].set_linestyle(':')

    # Customise the axis ticks
    ax.set_xticks([cx(0),cx(1),cx(2)])
    ax.set_xticklabels(['1 Jul','1 Aug','1 Sep'], rotation=0)
    ax.set_yticks([cy(100), cy(110), cy(120)])
    ax.set_yticklabels(['$100','$110','$120'], rotation=0)

    ax.set_ylim([cy(99.0), cy(125.0)])

    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')
