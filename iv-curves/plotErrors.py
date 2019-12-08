# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:43:13 2019

@author: 212569339
"""
#INPUTS: nested dictionary output from findErrors function
#{temp, innerDictionary}
#innerDictionary: data[temperature]= {"V":V,"errors":E}
#ADD'L INPUTS: regular nested dictionary
#outerDictionary = data.....data[temperature]= {"V":V,"I":I}

#OUTPUTS:Plots regular and log-log voltage and current curves with error bars

#matplotlib.pyplot.errorbar(x, y, yerr=None, xerr=None, fmt='', ecolor=None, elinewidth=None, capsize=None, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None, *, data=None, **kwargs)
#all inputs besides x and y are optional

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm


def plotErrors(data, errorData):
    cmap = plt.get_cmap('rainbow')
    cNorm  = colors.LogNorm(vmin=1, vmax=300)
    scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cmap)
    scalarMap._A = [] #this is needed to add a color bar later

    for T, dat in data.items():
        v = dat["V"]
        i = dat["I"]
        colorVal = scalarMap.to_rgba(T)
        for T, dat in errorData.items():
            error = dat["errors"]
            
            #Plot normal with errorbars on top
            plt.subplot(121)
            plt.errorbar(v, i, error, color=colorVal)
            
	
    plt.subplot(121)
    plt.ylabel("Current (A)")
    plt.xlabel("Voltage")
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    
    plt.colorbar(scalarMap,fraction=0.05,spacing='proportional',ticks=[1.6,2,5,10,50,100,200,300])
    plt.show()