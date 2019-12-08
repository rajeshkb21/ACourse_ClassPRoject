# ACourse_ClassProject
Team members: Rajesh Bollapragada, Yohan John, Katherine Quinn, David Jasinski, Marissa Brennan, Sriram Boppana, Travis Oneil, Cole Caynoski, Becky Sondelski, Emily Cheng, Hannah Bower, Katelyn Angeliu 

## Project Documentation
### Filtering Interference (Lean Filter)

The functions provided in the filter.py file were tested in the analysis.py file. The first function fft(v,i) was used in the consecutive function to transpose the 
current data from time to frequency space. The lowpass(v,i,cutoff) function is necessary to remove frequencies above a specified threshold. In our case we wanted to 
place a cutoff frequency at 50 Hz to remove the unnecessary high frequency noise to clean-up the data. The function also takes the inverse fft of the data to transpose the 
data into the time domain. The highpass(v,i,cutoff) function does just the same except now high frequencies pass through the filter and low frequencies below a particular 
threshold, in our case we selected a frequency of 0 Hz, which was filtered from our dataset. The bandpass(v,i, cutoff) function tested was used to place limitations on
both lower and upper frequency values. Bandpass filters specify a range in which the frequencies defined pass through the values centralized between the two cutoffs. Our cutoff values 
set for the bandpass filter were 0 Hz and 50 Hz. The notchfilter(v,i,cutoff_low, cutoff_high) function defines a low and a high frequency that can pass through and further
filters out everything encompassing the central range between the two frequency values. Filter cutoff ranges were defined as 45 Hz and 55 Hz.  

### FFT before filtering at 75k
![alt text](https://github.com/rajeshkb21/ACourse_ClassPRoject/blob/leanfilter/FFT_Nofilter75k.png)

### FFT after low pass (50Hz) at 75k
![alt text](https://github.com/rajeshkb21/ACourse_ClassPRoject/blob/leanfilter/FFT_Lowpass50Hz_75K.png)

### FFT after notch filter (45-55Hz) at 75k
![alt text](https://github.com/rajeshkb21/ACourse_ClassPRoject/blob/leanfilter/FFT_Notch_Filter_45_55Hz_75k.png)

### IV curve no filtering
![alt text](https://github.com/rajeshkb21/ACourse_ClassPRoject/blob/leanfilter/IV_Curve_75k.png)

### IV curve after filtering with low pass
![alt text](https://github.com/rajeshkb21/ACourse_ClassPRoject/blob/leanfilter/Full_IV_Curve_Lowpass_50Hz_75K.png)

### IV curve after filtering with notch filter
![alt text](https://github.com/rajeshkb21/ACourse_ClassPRoject/blob/leanfilter/Full_IV_Curve_Notch_45_55Hz_75K.png)

The analysis.py file requires importing the filters library in order for the filters functions to be applied. The key to implementing the functions in the main code is making sure 
the data is not averaged prior to applying the filters. Raw data from the {V,I} dictionaries should be the items treated by the filter. The first step necessary is to convert the 
values from time domain to frequency domain. If we pull up a single .txt file from the temperatures tested the first column explicitly shows voltage values, while the following 10 
right columns are corresponding current values to the voltage listed into the same row. We tried this for the single temperature of 75K. Data from a single row must be flattened to a single 
column in order to convert the data to the time domain from an i-v plot. Only a single voltage value should be represented for the time conversion step. Anything below or above the row in
the voltage column should be ignored when initially constructing and interpretting the for loop. The time or spacing between each of the rows are considered the x-axis values, while the current
values for the corresponding voltage are the y-values. The data itself represented in the time-domain should show some spikes representing noise in the data. 


### Leakage Current Offset Correction and Zero Point Resistance
When there is zero voltage placed across this circuit, ideally there should be no current through the circuit. However, there is a small leakage current across the circuit which offsets the remaining current data by a constant amount. 
To account for this, the file offset.py is used to subtract out any offset and make sure that the current is 0 Amps at all temperatures when there is 0 V input. 

In this file the numpy and scipy libraries are imported in order to run calculations on the given data, which is also imported. In this file, the initial voltage and current data extracted into arrays and then is reduced into only
the data where the voltage between +0.2V and -0.2V. A linear regression is then used on this section of the data and the y-intercept (leakage current) and slope (1/Resistance) of the linear regression is noted. The given voltage 
values are then taken and placed into a new array, while the current values are now adjusted by subtracting the y-intercept value from every given current value and placed into an array. The slope of the linear regression is also 
noted. These voltage and current arrays and slope values are recorded at each temperature using a for loop.

Once fully recorded, this data is returned to the main analysis script. When back in the analysis.py file, the corrected current values are plotted vs voltage at every temperature and the 0-point resistance at each temperature is 
plotted vs temperature.

### Temperature vs. Resistance and Power Through the Resistor
The numpy library is imported to aid in calculating Resistance and Power from the measured Voltage and Current values. Matplotlib is used to aid in plotting data.

The sole function within the python file, pwr.py, takes the dictionary (segmented by temperature) of dictionaries (segmented by data like Voltage and Current), adds a key and values for Power in the subdicitonary, and returns the new dictionary of dictionaries. Power through the resistor is found using the eqution: P = V*I.

The sole function within the python file, rbplt.py, takes the dictionary (segmented by temperature) of dictionaries (segmented by data like Voltage and Current) and plots them on a rainbow plot given data keys for each axis AND the label for each axis.

The sole funciton within the python file, pltRvT.py, takes the dictionary (segmented by temperature) of dictionaries (segmented by data like Voltage and Current), finds the Average resistance at each temperature using the formula: R = V/I, and plots Resistance versus Temperature.



### Error Analysis
The error analysis code consists of two main sections: the Linear Regression Definition and the Exponential Regression Defininition.

In the Linear Regression Definition section, the stats.lingress function is used to find the slope, intercept, r, p_value, std_err of the data. 
Then, the R-squared values are plotted vs. Temperature.

In the Exponential Regression Definition section, the np.squeeze function and the np.argwhere function are utilized to produce filtered voltage and current outputs.
The stats function is then used to find the R-value of the filtered outputs.
Finally,the R-squared values are plotted vs. Temperature.

The Linear Regression and Exponetial Regression plots as a function of temperature help determine at which temperatures the Linear Regression is a better fit compared to the Exponential Regression.

### Error Bars
The error bar code calculates the standard deviation of the current data for each voltage vaule, then plots those standard deviations as error bars on the IV curve. 
This visually indicates how much variation there is within the current measurements before they get collapsed to a single value.



## Team Member Contributions

 - Head Honcho: Yohan John Raj Bollabragada

###### Filtering
  - Code/Specialist: Sriram Boppana
  - Documentation/Product Owner: Marissa Brennan
  
###### Leakage Current Offset Correction and Zero Point Resistance:
 - Code/Specialist: Yohan John
 - Code/Scrum Master: Travis Oneil
 - Documentation/Product Owner: David Jasinski
 
###### Temperature vs. Resistance and Power Through the Resistor
 - Code/Scrum Master/Documentation: William (Cole) Caynoski
 - Code/Specialist/Product Owner: Emily Cheng

###### Error Analysis 
 - Code/Specialist: Becky Sondelski
 - Code/Scrum Master: Raj Bollapragada
 - Documentation/Product Owner: Hannah Bower
 
###### Error Bars
 - Code/Specialist: Katherine Quinn
 - Code/Specialist/Documentation: Katelyn Angeliu 
 

## Applications of Learnings

- With the functionality of Github as an opensource database, Github allows for the comparison of methods with other programmers and scientists. Therefore, an extension of this homework would be to compare data analysis techniques of similar data with other programers/scientists on the Github platform.

- Additionally, if the project was to be expanded to include other variables, Agile and Git hub would allow the team to add features easily and simultaneously.

- Furthermore, the Agile philosophy makes work focused and transparent so when new tasks are given, there is no confusion and there is a clear flow for how to solve the problems.


## Agile Retrospective

- Delta: More technical introduction
  Suggestion: Walk us through the Git hub structure and commonly used commands during the class period

- Delta: more detailed Github background 
  Suggestion: Give more details and descriptions on how Github is structurally setup and runs in the class period

