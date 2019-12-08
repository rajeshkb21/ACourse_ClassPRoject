# ACourse_ClassProject
Team members: Rajesh Bollapragada, Yohan John, Katherine Quinn, David Jasinski, Marissa Brennan, Sriram Boppana, Travis Oneil, Cole Caynoski, Becky Sondelski, Emily Cheng, Hannah Bower, Katelyn Angeliu 

## Project Documentation
Filtering Interference (Lean Filter)

The functions provided in the filter.py file were tested in the analysis.py file. The first function fft(v,i) was used in the consecutive function to transpose the 
current data from time to frequency space. The lowpass(v,i,cutoff) function is necessary to remove frequencies above a specified threshold. In our case we wanted to 
place a cutoff frequency at 50 Hz to remove the unnecessary high frequency noise to clean-up the data. The function also takes the inverse fft of the data to transpose the 
data into the time domain. The highpass(v,i,cutoff) function does just the same except now high frequencies pass through the filter and low frequencies below a particular 
threshold, in our case we selected a frequency of 0 Hz, which was filtered from our dataset. The bandpass(v,i, cutoff) function tested was used to place limitations on
both lower and upper frequency values. Bandpass filters specify a range in which the frequencies defined pass through the values centralized between the two cutoffs. Our cutoff values 
set for the bandpass filter were 0 Hz and 40 Hz. The notchfilter(v,i,cutoff_low, cutoff_high) function defines a low and a high frequency that can pass through and further
filters out everything encompassing the central range between the two frequency values. Filter cutoff ranges were defined as 45 Hz and 55 Hz.  

![alt text] https://github.com/rajeshkb21/ACourse_ClassPRoject/blob/leanfilter/FFT_Nofilter75k.png


The analysis.py file requires importing the filters library in order for the filters functions to be applied. The key to implementing the functions in the main code is making sure 
the data is not averaged prior to applying the filters. Raw data from the {V,I} dictionaries should be the items treated by the filter. The first step necessary is to convert the 
values from time domain to frequency domain. If we pull up a single .txt file from the temperatures tested the first column explicitly shows voltage values, while the following 10 
right columns are corresponding current values to the voltage listed into the same row. We tried this for the single temperature of 75K. Data from a single row must be flattened to a single 
column in order to convert the data to the time domain from an i-v plot. Only a single voltage value should be represented for the time conversion step. Anything below or above the row in
the voltage column should be ignored when initially constructing and interpretting the for loop. The time or spacing between each of the rows are considered the x-axis values, while the current
values for the corresponding voltage are the y-values. The data itself represented in the time-domain should show some spikes representing noise in the data. 


## Team Member Contributions

## Applications of Learnings

## Agile Retrospective
