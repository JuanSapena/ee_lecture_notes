import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

import random
import pickle
from matplotlib.patches import Rectangle

from . import base

def figure1_generate_data(config):
    target_folder = config['figures folder']+config['tools']['data folder']
    filename = 'noise_realisations.pkl'
    print("Generating data for chapter 2, figure 1", filename)

    # Set seed for reproducibility
    np.random.seed(1)

    T=100
    N=5
    m=1.

    noise=pd.DataFrame(np.random.normal(0,1,size=[N,T+1]),index=range(1,N+1))
    x=pd.DataFrame(index=range(1,N+1),columns=range(0,T+1))
    x.iloc[:,0]=np.random.normal(0,1,size=N)

    for t in range(1,T+1):
        x.iloc[:,t]=x.iloc[:,t-1]*(1-m)+noise.iloc[:,t-1]

    x.to_pickle(target_folder+filename)
    return 0


def figure1(config):
    target_folder = config['figures folder']+config['tools']['output folder']
    data_folder = config['figures folder']+config['tools']['data folder']
    filename = 'sp_grid.pdf'
    print("Plotting chapter 2, figure 1", filename)

    # Read in data that has been generated previously
    x=pd.read_pickle(data_folder+"noise_realisations.pkl")
    T = len(x.iloc[1,:])
    t = np.arange(T)

    # Create plot
    fig, ax = plt.subplots(1,1)
    base.set_style(config)
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    c1 = colors[0]
    c2 = colors[1]
    c3 = colors[2]

    # Add lines to the plot
    for i in [0,1, 2, 3, 4 ]:
        offset = i*10
        ax.plot(x.iloc[i,:] + offset, linestyle='-', color=c1)
        label = '$y_'+str(i+1)+'(t)$'
        ax.annotate(s=r"{}".format(label),xy=(0,offset),xytext=(-11, offset))
    ax.annotate(s=r'$y_1(t^*)$',xy=(50, 0),xytext=(43.5, 5),\
        arrowprops=dict(arrowstyle='->',color='black'))
    # Draw x axis line
    ax.arrow(0, -3.5, T, 0, head_width=1, head_length=2, linewidth=2, color=c2, clip_on=False)
    # Draw y axis line
    ax.arrow(-13.5, 0, 0, 42.5, head_width=2, head_length=1, linewidth=2, color=c3, clip_on=False)


    ax.set_xlabel('time, t')
    ax.set_ylabel('realisation, i')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.yaxis.set_label_coords(-0.1, 0.5)

    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')

    # Final tweaks and save
    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    return fig, ax

def figure2(config):
    target_folder = config['figures folder']+config['tools']['output folder']
    data_folder = config['figures folder']+config['tools']['data folder']
    filename = 'ergodic_grid.pdf'
    print("Plotting chapter 2, figure 2", filename)

    # Get colors from the current style
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    c1 = colors[0]
    c2 = colors[1]
    c3 = colors[2]

    # Read in data that has been generated previously
    x=pd.read_pickle(data_folder+"noise_realisations.pkl")
    T = len(x.iloc[1,:])
    t = np.arange(T)

    # Create plot. We call the previous function that generates figure 1 since
    # we want to add additional features to that plot.
    fig, ax = figure1(config)

    ax.add_patch( Rectangle((0.0, 17),
                        T, 6,
                        fc =c2,
                        ec ='none',
                        alpha=0.25) )
    ax.add_patch( Rectangle((43, -3),
                        13, 53,
                        fc =c3,
                        ec ='none',
                        alpha=0.25) )


    # Final tweaks and save
    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')
    return 0
