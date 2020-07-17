import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

import random
import pickle

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

    fig, ax = plt.subplots(1,1)
    base.set_style(config)

    # Add lines to the plot
    ax=x.iloc[1,:].plot(linestyle='-',color='blue')
    ax.plot(t,x.iloc[2,:]-10,linestyle='-',color='blue')
    ax.plot(t,x.iloc[3,:]-20,linestyle='-',color='blue')
    ax.plot(t,x.iloc[4,:]-30,linestyle='-',color='blue')
    ax.plot(t,x.iloc[0,:]-40,linestyle='-',color='blue')

    # Final tweaks and save
    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    return 0
