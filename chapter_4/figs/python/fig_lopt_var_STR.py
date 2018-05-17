#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:54:25 2018

@author: obp48
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

data_ID="STR-FED"
input_dir="./../../../../Leverage_Efficiency/data/"
lopt_var=pd.read_pickle(input_dir+data_ID+"_lopt_var.pkl")
#lopt_2=pd.read_pickle(input_dir+data_ID+"-2_lopt_exp.pkl")
#lopt_3=pd.read_pickle(input_dir+data_ID+"-3_lopt_exp.pkl")
#
#rel_ret_1=pd.read_pickle(input_dir+data_ID[0:3]+"_returns.pkl")
#rel_ret_2=pd.read_pickle(input_dir+data_ID[4:7]+"_returns.pkl")
#
returns_1=pd.read_pickle(input_dir+data_ID+"-1.pkl")
equity_1=np.cumprod(returns_1)
final_equity_1=equity_1[-1:].T
#
#start_date=max(min(rel_ret_1.index),min(rel_ret_2.index))
#end_date=min(max(rel_ret_1.index),max(rel_ret_2.index))
#
#rel_ret=rel_ret_1[start_date:end_date]-rel_ret_2[start_date:end_date]
#
para=np.polyfit(final_equity_1.index[25:-25],np.log(final_equity_1.iloc[25:-25]),2)
Delta_t=returns_1.index[-1] - returns_1.index[0]
years=Delta_t.days/365.25
sigma=np.sqrt(-2*para[0][0]/years)
#mu_e=para[1][0]/years
#mu_r=para[2][0]/years
#lopt_est=mu_e/(sigma*sigma)
#st_err=1./(sigma*np.sqrt(years))
#
#print(lopt_1.index[0],lopt_1.index[-1])
#print("sigma=",sigma,"mu_e=",mu_e,"lopt_est=",lopt_est,"+-",st_err)

#### growth rate vs. leverage ####
fig=plt.figure()

#Delta_t=returns_1.index[-1] - returns_1.index[0]
#years=Delta_t.days/365.25
#ax=(lopt.plot(label='model 1', linewidth=5)
plt.loglog(lopt_var.index.days,(lopt_var.index.days/365.25)**(-0.5)/sigma,linestyle='--',label='prediction')
plt.loglog(lopt_var.index.days,np.sqrt(lopt_var),color='red',marker='o',linestyle='')
#plt.plot(lopt_1.index,1-1./np.sqrt(sigma*sigma*(lopt_1.index-lopt_1.index[0]).days/365.25),color='pink',linestyle='--')
#plt.plot(lopt_1.index,1+2./np.sqrt(sigma*sigma*(lopt_1.index-lopt_1.index[0]).days/365.25),color='pink',linestyle=':')
#plt.plot(lopt_1.index,1-2./np.sqrt(sigma*sigma*(lopt_1.index-lopt_1.index[0]).days/365.25),color='pink',linestyle=':')
#plt.plot(lopt_1, label='model 1')
#plt.plot(lopt_2, label='model 2')
#plt.plot(lopt_3, label='model 3')
#(np.log(final_equity_2.iloc[:,0].astype(float))/years).plot(label='model 2', linewidth=3)
#(np.log(final_equity_3.iloc[:,0].astype(float))/years).plot(label='model 3', linewidth=1)
#ax.set_yscale('log')
#plt.xlim([final_equity_1.index.min(),final_equity_1.index.max()])
#plt.ylim([-1.5,2.2])
#vals = ax.get_yticks()
#ax.set_yticklabels(['{:3.0f}% p.a.'.format(100*x) for x in vals])
#ax.set_aspect(1./(1.618*ax.get_data_ratio()))
#plt.title('some title')
plt.xlabel('window size')
plt.ylabel('standard deviation of optimal leverage')
#plt.axhline(y=1,linestyle=':',color='grey',linewidth=.5)
#plt.axhline(y=0,linestyle=':',color='grey',linewidth=.5)
#plt.axvline(x=1.68045,linestyle='--',color='grey',linewidth=1)
plt.legend(loc=1, bbox_to_anchor=(.55,.3))
#ax.legend_.remove()
plt.xlim([10,7000])
plt.ylim([.1,1000])
plt.savefig("./../"+data_ID+"_lopt_var.pdf", bbox_inches='tight')
plt.savefig("./../"+data_ID+"_lopt_var.jpg", bbox_inches='tight')
plt.show()
#plt.xlim([-.5,1.55])
#vals = ax.get_yticks()
#ax.set_yticklabels(['{:3.0f}% p.a.'.format(100*x) for x in vals])
##ax.set_aspect(1./(1.618*ax.get_data_ratio()))
##plt.title('some title')
#plt.xlabel('leverage')
#plt.ylabel('annual rate of return')
#plt.axvline(x=0,linestyle=':',color='grey',linewidth=.5)
#plt.axhline(y=0,linestyle=':',color='grey',linewidth=.5)
#plt.axvline(x=1.68045,linestyle='--',color='grey',linewidth=1)
##plt.legend(loc=1, bbox_to_anchor=(.55,.5))
#ax.legend_.remove()
##plt.savefig("./BTC_return.pdf", bbox_inches='tight')
#plt.show()
#plt.show()