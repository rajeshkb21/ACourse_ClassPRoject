"""
Demo Analysis Project
Written by Isabelle Jansen
Based off the work done for master's project
https://openaccess.leidenuniv.nl/handle/1887/43976
"""

#Import various modules
import os
import re

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm

import calculateErrors
import plotErrors
import offset
import pwr
import rbplt
import pltRvT

#Step 2: "Collapse" the files to have single I/V pair instead of trace/retrace
def collapse_iv(fileV,fileI):
	V = np.unique(fileV)
	I = []
	for volt in V:
		I.append(np.mean(fileI[fileV==volt]))
	return (V,np.array(I))


#Step 1: Load all the files
data = {}
errorData = {}

#Files must end in ".txt" to be considered.
#Use simple regular expression to grab temperature
#Test patterns matching regex using https://regex101.com/
regex = '^([\d\.]+)[Kk]\.txt$'

for file in os.listdir('data'):
    #Checks if file name matches pattern
    good_file = re.search(regex,file)
    
    if good_file:
        
        #If so, pattern grabbed the temperature as a "group"
        temperature = float(good_file.groups()[0])	
        
        #Load the file using numpy loadtxt to put into array
        file_data = np.loadtxt('data/'+file,skiprows=3).transpose()
        
        #First column is voltage...
        fileV = file_data[0,:]
        
        #And the other 10 are all current
        fileI = np.mean(file_data[1:,:],0)
                
        #See Step 2 for this
        V, I = collapse_iv(fileV,fileI)
        errors = calculateErrors(fileV,fileI)
        
        data[temperature] = {"V":V,"I":I}
        
        errorData[temperature] = {"V":V, "errors":errors}

#Step 3: Analysis
# Get creative!

data = pwr.add_power_to_dict(data)


data_offset = offset.correct_offset(data)  #Import offset data

#Step 4: Plotting loaded files

#Make a new window attempting to get rid of those dumb warnings
fig = plt.figure()
plotErrors(data, errorData)

#set the color map, and normalize it on a log scale from 1 to 300
#Color represents the temperature of the measurement
cmap = plt.get_cmap('rainbow')
cNorm  = colors.LogNorm(vmin=1, vmax=300)
scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cmap)
scalarMap._A = [] #this is needed to add a color bar later

fig, (ax1,ax2) = plt.subplots(1,2)
for T, dat in data.items():
	v = dat["V"]
	i = dat["I"]
	colorVal = scalarMap.to_rgba(T)
	
	#Plot normally
	ax1.plot(v,i,color=colorVal)
	
	#Plot on a log-log scale to see exponential part of the curve
	ax2.loglog(v,np.abs(i),color=colorVal)
	
ax1.set_ylabel("Current (A)")
ax1.set_xlabel("Voltage")
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

ax2.set_xlabel("Voltage")

plt.colorbar(scalarMap,fraction=0.05,spacing='proportional',ticks=[1.6,2,5,10,50,100,200,300])

plt.show()
plt.close(fig)

# Offet Starts
#fig = plt.figure(2)
#plt.plot(data[300]['V'],data[300]['I'],color='red')
#plt.plot(data_offset[300]['V'],data_offset[300]['I'],color='blue')
#plt.ylabel("Current (A)")
#plt.xlabel("Voltage")
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.legend('Original','Offset')

Temp = []   #Create Temperature vector for graph
R_zero = []   #Create zero point resistance vector
for T,dat in data_offset.items():   #At each temperature tested
    Temp.append(T)                  #Append the temperature vector
    R_zero.append(dat['R'])         #Append the resistance vector
    
plt.figure()
plt.scatter(Temp,R_zero)     #Scatter plot zero point resistance vs temperature
plt.ylabel("0-Point Resistance (Ohms)") #Resistance on the y axis
plt.xlabel("Temperature (K)")           #Temperature on the x axis
# Offset Ends

# # write the plotting funciton like: 
# #       plot_rainbow_like(data,xKey,yKey,xLabel,yLabel)
# rbplt.plot_rainbow_like(data,'V','P','Voltage','Power')

# #plotting resistance versus temperature
# pltRvT.plot_resistanceVtemperature(data)

# for T, dat in data.items():
# 	v = dat["V"]
# 	i = dat["I"]
# 	colorVal = scalarMap.to_rgba(T)
	
# 	#Plot normally
# 	plt.subplot(121)
# 	plt.plot(v,i,color=colorVal)
	
# 	#Plot on a log-log scale to see exponential part of the curve
# 	plt.subplot(122)
# 	plt.loglog(v,np.abs(i),color=colorVal)
	
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
# plt.close(fig)

