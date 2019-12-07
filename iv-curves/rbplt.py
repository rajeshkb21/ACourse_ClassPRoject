# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:50:10 2019

@author: 212767297
"""

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm


def plot_rainbow_like(Data,xKey,yKey,xLabel,yLabel,limits='Default',title=''):
    # Data needs to be a dictionary of dictionaries of 1D numpy arrays with the same number of keys
    
    fig = plt.figure()

    #set the color map, and normalize it on a log scale from 1 to 300
    #Color represents the temperature of the measurement
    cmap = plt.get_cmap('rainbow')
    cNorm  = colors.LogNorm(vmin=1, vmax=300)
    scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cmap)
    scalarMap._A = [] #this is needed to add a color bar later
    
    tKeys = list(Data.keys())
    
    for temp in tKeys:
    	x = Data[temp][xKey]
    	y = Data[temp][yKey]
    	colorVal = scalarMap.to_rgba(temp)
    	
    	#Plot normally
    	plt.plot(x,y,color=colorVal)
    	
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.title(title)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    
    plt.colorbar(scalarMap,fraction=0.05,spacing='proportional',ticks=[1.6,2,5,10,50,100,200,300])
    
    plt.show()
    plt.close(fig)