import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

import random
import pickle

from . import base

def figure1_generate_data(config):
    target_folder = config['figures folder']+config['why']['data folder']
    filename = 'coin_ensemble.pkl'
    print("Generating data for chapter 1, figure 1", filename)
    T = 52+1
    N_ensemble=1000000

    ensemble = pd.DataFrame(index=np.arange(0,N_ensemble),columns=np.arange(0,T))
    ensemble.iloc[:,0]=np.ones(N_ensemble)

    # T multiplicative repetitions
    # Set seed for reproducibility
    np.random.seed(1)
    for t in range(1, T):
        # 50% chance of 0.6x what we had before, or
        # 50% chance of 1.5x what we had before.
        ensemble.iloc[:,t]=ensemble.iloc[:,t-1] * np.random.choice([0.6, 1.5],size=N_ensemble)
    ensemble.to_pickle(target_folder+filename)
    return 0

def figure3_generate_data(config):
    target_folder = config['figures folder']+config['why']['data folder']
    filename = 'coin_20_years.pkl'
    print("Generating data for chapter 1, figure 3", filename)
    T = 1040
    N_ensemble=1

    ensemble = pd.DataFrame(index=np.arange(0,N_ensemble),columns=np.arange(0,T))
    ensemble.iloc[:,0]=np.ones(N_ensemble)

    # T multiplicative repetitions
    # Set seed for reproducibility
    np.random.seed(1)
    for t in range(1, T):
        # 50% chance of 0.6x what we had before, or
        # 50% chance of 1.5x what we had before.
        ensemble.iloc[:,t]=ensemble.iloc[:,t-1] * np.random.choice([0.6, 1.5],size=N_ensemble)
    ensemble.to_pickle(target_folder+filename)
    return 0

def figure1(config):

    target_folder = config['figures folder']+config['why']['output folder']
    data_folder = config['figures folder']+config['why']['data folder']
    filename = 'x_of_t_lin_1.pdf'
    print("Plotting chapter 1, figure 1", filename)

    fig, ax = plt.subplots(1,1)
    base.set_style(config)

    # Read in data that has been generated previously
    ensemble=pd.read_pickle(data_folder+"coin_ensemble.pkl")
    T = len(ensemble.iloc[1,:])
    x = np.arange(T)

    # Add line to axis
    ax.plot(x, ensemble.iloc[45,:], label='$N=1$')

    # Customise axes etc
    ax.set_xlim((0,max(ensemble.columns)))
    ax.legend()
    ax.set_xlabel('$t$')
    ax.set_ylabel('$x(t)$')

    # Final tweaks and save
    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    return 0


def figure2(config):

    target_folder = config['figures folder']+config['why']['output folder']
    data_folder = config['figures folder']+config['why']['data folder']

    base.set_style(config)
    # Read in data that has been generated previously
    ensemble=pd.read_pickle(data_folder+"coin_ensemble.pkl")
    T = len(ensemble.iloc[1,:])
    x = np.arange(T)
    # Perform averages over increasing numbers of realisations
    w1 = ensemble.iloc[45,:]
    w100 = np.mean(ensemble.iloc[0:100,:])
    w10K = np.mean(ensemble.iloc[0:10000,:])
    w1M = np.mean(ensemble)


    # Generate first subpanel: linear scale
    filename = 'x_of_t_lin.pdf'
    print("Plotting chapter 1, figure 2 (A)", filename)
    fig, ax = plt.subplots(1,1)

    # Add lines to axis
    ax.plot(x, w1, label='$N=1$')
    ax.plot(x, w100, label='$N=100$')
    ax.plot(x, w10K, label='$N=10,000$')
    ax.plot(x, w1M, 'k', label='$N=1,000,000$')

    # Customise axes etc
    ax.legend()
    ax.set_xlabel('$t$')
    ax.set_ylabel('$x(t)$')

    # Final tweaks and save
    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    # Generate second subpanel: log scale
    filename = 'x_of_t_log.pdf'
    print("Plotting chapter 1, figure 2 (B)", filename)
    fig, ax = plt.subplots(1,1)


    # Add lines to axis
    # We will use the custom tplot() function to transform the axes to semilog.
    # First define the transformations to be applied to each axis
    def cx(x):
        return x

    def cy(x):
        return np.log10(x)

    ax = base.tplot(x, w1, cx, cy, ax, yticks='log', label = '$N = 1')
    ax = base.tplot(x, w100,  cx, cy, ax, yticks='log', label = '$N = 100')
    ax = base.tplot(x, w10K, cx, cy, ax, yticks='log', label = '$N = 10,000')
    ax = base.tplot(x, w1M, cx, cy, ax, yticks='log', label = '$N = 1,000,000')


    # Customise axes etc
    ax.legend()
    ax.set_xlabel('$t$')
    ax.set_ylabel('$x(t)$')

    # Final tweaks and save
    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    return 0

def figure3(config):

    target_folder = config['figures folder']+config['why']['output folder']
    data_folder = config['figures folder']+config['why']['data folder']

    base.set_style(config)
    # Read in data that has been generated previously
    ensemble=pd.read_pickle(data_folder+"coin_20_years.pkl")
    T = len(ensemble.iloc[0,:])
    x = np.arange(T)

    # Generate first subpanel: linear scale
    filename = 'x_of_t_lin_20_year.pdf'
    print("Plotting chapter 1, figure 3 (A)", filename)
    fig, ax = plt.subplots(1,1)
    # Add lines to axis
    ax.plot(x, ensemble.iloc[0,:],  label='$N=1$')

    # Customise axes etc
    ax.legend()
    ax.set_xlabel('$t$')
    ax.set_ylabel('$x(t)$')

    # Final tweaks and save
    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    # Generate second subpanel: log scale
    filename = 'x_of_t_log_20_year.pdf'
    print("Plotting chapter 1, figure 3 (B)", filename)
    fig, ax = plt.subplots(1,1)

    # Add lines to axis
    # We will use the custom tplot() function to transform the axes to semilog.
    # First define the transformations to be applied to each axis
    def cx(x):
        return x

    def cy(x):
        return np.log10(x)

    ax = base.tplot(x, ensemble.iloc[0,:], cx, cy, ax, yticks='log', label = '$N = 1')

    # Customise axes etc
    ax.legend()
    ax.set_xlabel('$t$')
    ax.set_ylabel('$x(t)$')

    # Final tweaks and save
    fig, ax =  base.apply_tweaks(config, fig, ax)
    plt.savefig(target_folder+filename, bbox_inches='tight')

    return 0
