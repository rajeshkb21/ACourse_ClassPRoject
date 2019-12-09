# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:18:14 2019

pltRvT.py

@author: 212767297
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_resistanceVtemperature(data, ax):
    Temp=[]
    avgresist=[]
    for T, dat in data.items():
        v = dat["V"]
        i = dat["I"]
        resist = np.divide(v,i)
        avgresist.append(np.mean(resist))
        Temp.append(T)
    
    fig = plt.figure()
    ax.scatter(Temp,avgresist)
    ax.set_ylim(0,1E7)
    ax.set_xlim(0,310)
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Resistance (ohms)")
    return