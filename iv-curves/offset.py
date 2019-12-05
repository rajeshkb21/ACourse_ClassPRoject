# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:33:18 2019

@author: 212767355
"""

import numpy as np
from scipy import stats
import matplotlib as plt

def correct_offset(data):   #create data with corrected offset
    
    data_offset = {}       #create data offset dictionary
    
    for T, dat in data.items():  #At every temperature value
        dat_off = {}
        
        v = np.array(dat['V'])   #Create voltage array
        i = np.array(dat['I'])   #Create current array
        vrang = v[(v >= -0.2) & (v <= 0.2)]  #Reduce voltage data to data in desired range
        irang = i[(v >= -0.2) & (v <= 0.2)]  #Reduce current data to data in desired range
        slope,interc,_,_,_ = stats.linregress(vrang,irang)  #Record slope and y-intercept of linear regressions of the data
        
        dat_off['V'] = dat['V']
        dat_off['I'] = dat['I'] - interc  #Subtracting the leakage current offset 
        dat_off['R'] = 1/slope  #Resistance is the reciprocal of the linear regression slopes
        
        data_offset[T] = dat_off
        
    return data_offset  #Returning offset data to the main analysis file
