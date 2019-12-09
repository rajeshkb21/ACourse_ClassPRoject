import os
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import filters
import calculateErrors
import plotErrors
import offset
import pwr
import rbplt
import pltRvT
import regression_analysis


def generate_filter_figure(data, file_data):
    
    pI = np.transpose(file_data[1:,:])
    fileV = file_data[0,:]
    fileI = np.mean(file_data[1:,:],0)
    fileV, fileI = filters.notchfilter(fileV,fileI,45,55)

    fig = plt.figure()
    fig.suptitle("Filtering Interference Analysis at 75K")

    ax1 = fig.add_subplot(421)
    ax2 = fig.add_subplot(422)
    ax3 = fig.add_subplot(423)
    ax4 = fig.add_subplot(424)
    ax5 = fig.add_subplot(425)
    ax6 = fig.add_subplot(426)
    ax7 = fig.add_subplot(427)

    ax1.title.set_text("FFT")
    ax2.title.set_text("Low-pass Filter FFT")
    ax3.title.set_text("Low-pass Filter")
    ax4.title.set_text("High-pass Filter FFT")
    ax5.title.set_text("High-pass Filter")
    ax6.title.set_text("Notch Filter FFT")
    ax7.title.set_text("Notch Filter")

    # FFT 75k
    for col in range(0,pI.shape[1]):
        mapV, mapI = filters.fft(fileI,pI[:,col])
        ax1.plot(mapV,mapI)
        ax1.set_xlim([0,100])

    # Low Pass Filter 75k
    for col in range(0,pI.shape[1]):
        mapV, mapI = filters.lowpass(fileV,pI[:,col],50)
        mapV2, mapI2 = filters.fft(mapV,mapI)
        ax2.plot(mapV2,mapI2)
        ax2.set_xlim([0,100])

    for col in range(0,pI.shape[1]):
        mapV, mapI = filters.lowpass(fileV,pI[:,col],50)
        ax3.plot(mapV,mapI)
        ax3.set_xlim([-1,1])

    # High Pass Filter 75k
    for col in range(0,pI.shape[1]):
        mapV, mapI = filters.highpass(fileV,pI[:,col],50)
        mapV2, mapI2 = filters.fft(mapV,mapI)
        ax4.plot(mapV2,mapI2)
        ax4.set_xlim([0,100])

    for col in range(0,pI.shape[1]):
        mapV, mapI = filters.highpass(fileV,pI[:,col],50)
        ax5.plot(mapV,mapI)
        ax5.set_xlim([-1,1])

    # Notch Filter 75k
    for col in range(0,pI.shape[1]):
        mapV, mapI = filters.notchfilter(fileV,pI[:,col],45,55)
        mapV2, mapI2 = filters.fft(mapV,mapI)
        ax6.plot(mapV2,mapI2)
        ax6.set_xlim([0,100])
        
    for col in range(0,pI.shape[1]):
        mapV, mapI = filters.notchfilter(fileV,pI[:,col],45,55)
        ax7.plot(mapV,mapI)
        ax7.set_xlim([-1,1]) 
    
    fig.tight_layout()
    plt.show()  
    return


def generate_offset_figure(data):
    supplemental_data = pwr.add_power_to_dict(data)
    data_offset = offset.correct_offset(supplemental_data)
    Temp = []   #Create Temperature vector for graph
    R_zero = []   #Create zero point resistance vector
    for T,dat in data_offset.items():   #At each temperature tested
        Temp.append(T)                  #Append the temperature vector
        R_zero.append(dat['R'])         #Append the resistance vector
        
    plt.figure()
    plt.scatter(Temp,R_zero)     #Scatter plot zero point resistance vs temperature
    plt.ylabel("0-Point Resistance (Ohms)") #Resistance on the y axis
    plt.xlabel("Temperature (K)")           #Temperature on the x axis
    plt.show()
    return supplemental_data


def generate_resistance_power_figure(data):
    fig = plt.figure()
    fig.suptitle("Resistance and Power Figures")
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    pltRvT.plot_resistanceVtemperature(data, ax1)
    rbplt.plot_rainbow_like(data,'V','P','Voltage','Power', ax2)
    fig.tight_layout()    
    plt.show()
    return


def generate_regression_figure(data):
    fig = plt.figure()
    fig.suptitle("Resistance and Power Figures")
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    regression_analysis.linear_regression(data, ax1)
    regression_analysis.exponential_regression(data, ax2)
    plt.show()
    return


def generate_error_bar_figure(data,error_data):
    plotErrors.plotErrors(data, error_data)
    return


if __name__ == "__main__":
    plt.ioff()
    data, file_data, error_data = regression_analysis.import_data()
    # Filtering Interference
    generate_filter_figure(data, file_data)
    # Leakage Current Offset
    supplemental_data = generate_offset_figure(data)
    # # Resistance Temperature and Power
    generate_resistance_power_figure(supplemental_data)
    # # Regression Analysis
    generate_regression_figure(data)
    # # Error Bars
    generate_error_bar_figure(data, error_data)