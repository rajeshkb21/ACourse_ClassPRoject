# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:00:24 2019

@author: 212569339
"""
# INPUTS:{temp, innerDictionary}
#		innerDictionary data[temperature]= {"V":V,"I":I}
# OUTPUT: {temp, innerDictionary}
#		innerDictionary data[temperature]= {"V":V,"errors":E}

from plotErrors import *

def calculateErrors(file_data):
	#First column is voltage...
	fileV = file_data[0,:]
	
	#And the other 10 are all current
	fileI = file_data[1:,:]
		
	#See Step 2 for this
	#V, errors = collapse_iv(fileV,fileI) 
	V = np.unique(fileV)
	errors = []
	for volt in V:
		errors.append(np.std(fileI[fileV==volt]))
	
	error_data[temperature] = {"V":V,"errors":np.arrays(errors)}

	plotErrors(data, error_data)
	# V = np.unique(fileV)
	# errors = []
	# for volt in V:
		# errors.append(np.std(fileI[fileV==volt]))
	# return (V,np.array(errors))

		




    # for T, dat in data.items():
        # v = dat["V"]
        # i = dat["I"]
        # colorVal = scalarMap.to_rgba(T)
    # for T, dat in errorData.items():
        # error = dat["errors"]
        
    	# #Plot normal with errorbars on top
    	# plt.subplot(121)
    	# plt.errorbar(v, i, error, color=colorVal)
        
    	# #Plot on a log-log scale to see exponential part of the curve
        # plt.subplot(122)
    	# plt.loglog(v,np.abs(i),np.abs(error), color=colorVal)
    	
        
    # plt.subplot(121)
    # plt.ylabel("Current (A)")
    # plt.xlabel("Voltage")
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    
    # plt.subplot(122)
    # plt.ylabel("Current (A)")
    # plt.xlabel("Voltage")
    # axis = list(plt.axis())
    # axis[0] = 4e-3
    # plt.axis(axis)
    
    # plt.colorbar(scalarMap,fraction=0.05,spacing='proportional',ticks=[1.6,2,5,10,50,100,200,300])
    
    # plt.show()