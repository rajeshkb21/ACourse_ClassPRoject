import numpy
"""For fun/reference: Functions to apply various frequency filters to the data"""

sample_rate = 1000 #Hz
def fft(v,i):
    v,i = self.get_iv()
    fy = np.abs(numpy.fft.rfft(i))
    fx = numpy.fft.rfftfreq(i.size, d=1./sample_rate)
    return fx, fy

def lowpass(v,i,cutoff):
    fx, fy = fft(v,i)
    fy[fx > cutoff] = 0
    i_lowpass = numpy.fft.irfft(fy)
    return v, i_lowpass

def highpass(v,i,cutoff):
    fx, fy = fft(v,i)
    fy[fx < cutoff] = 0
    i_highpass = numpy.fft.irfft(fy)
    return v, i_highpass

def bandpass(v,i,cutoff_low, cutoff_high):
    fx, fy = fft(v,i)
    fy[numpy.logical_or(fx<cutoff_low,fx>cutoff>high)] = 0
    i_bandpass = numpy.fft.irfft(fy)
    return v, i_bandpass
    
def notchfilter(v,i,cutoff_low, cutoff_high):
    fx, fy = fft()
    fy[numpy.logical_and(fx > cutoff_low,fx < cutoff_high)] = 0
    i_notchfilter = numpy.fft.irfft(fy)
    return v, i_notchfilter