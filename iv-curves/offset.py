# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:33:18 2019

@author: 212767355
"""

import numpy as np
from scipy import stats
import matplotlib as plt

def correct_offset(data):
    
    data_offset = {}
    
    for T, dat in data.items():
        dat_off = {}
        
        v = np.array(dat['V'])
        i = np.array(dat['I'])
        vrang = v[(v >= -0.2) & (v <= 0.2)]
        irang = i[(v >= -0.2) & (v <= 0.2)]
        slope,interc,_,_,_ = stats.linregress(vrang,irang)
        
        dat_off['V'] = dat['V']
        dat_off['I'] = dat['I'] - interc
        dat_off['R'] = 1/slope
        
        data_offset[T] = dat_off
        
    return data_offset
