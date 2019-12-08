# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:18:14 2019

pltRvT.py

@author: 212767297
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_resistanceVtemperature(data):
    Temp=[]
    avgresist=[]
    for T, dat in data.items():
        v = dat["V"]
        i = dat["I"]
        resist = np.divide(v,i)
        avgresist.append(np.mean(resist))
        Temp.append(T)
    
    fig = plt.figure()
    plt.scatter(Temp,avgresist)
    plt.ylim(0,1E7)
    plt.xlim(0,310)
    plt.xlabel("Temperature (K)")
    plt.ylabel("Resistance (ohms)")
    
    plt.show()
    plt.close(fig)
    return