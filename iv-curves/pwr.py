# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:33:24 2019

Power versus voltage and temperature

@author: 212767297
"""

def add_power_to_dict(tempDictOfDataDict):
    temperatureKeys = list(tempDictOfDataDict.keys())
    for i in range(0,len(temperatureKeys)):
        # current key is I and voltage key is V
        key = temperatureKeys[i]
        V = tempDictOfDataDict[key]['V']
        I = tempDictOfDataDict[key]['I']
        tempDictOfDataDict[key]['P'] = V*I
    
    return tempDictOfDataDict


if __name__ == '__main__':
    print('THE POWER FUNCTION')