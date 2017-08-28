import numpy as np
import matplotlib.pyplot as plt
import os
from argparse import ArgumentParser

#~~~~~~~~~~~~~~~~~~~~Command Line Arguments~~~~~~~~~~~~~~~~~~~

"""parser = ArgumentParser("This script plots spectra from a HackRF One generated binary file")
parser.add_argument('-i', action='store', dest='init_freq', type=float, required=True, help='center frequency of first sampling')
parser.add_argument('-b', action='store', dest='bands', type=int, default=1, help='number of samplings')
parser.add_argument('-t', action='store', dest='transfer', type=bool, default=False, help='run the hackrf_transfer command')
parser.add_argument('-s', action='store', dest='samp_rate', type=int, default=20000000, help='sampling rate')
parser.add_argument('-f', action='store', dest='fftsize', type=int, default=131072, help='twice the fft averaging size')
parser.add_argument('-m', action='store', dest='median', type=int, default=10, help='half the median-averaging to reduce data')

args = parser.parse_args()
bands = args.bands
init_freq = args.init_freq
transfer = args.transfer
samp_rate = args.samp_rate
fftsize = args.fftsize
m = args.median

#~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~"""

def hackrf_transfer(init_freq, bands, samp_rate, timeout=5, lgain=24, gain=30):
    i = 0
    while i < bands:
        center_freq = init_freq + (i*samp_rate/2)
        os.system("timeout " + str(timeout) +"s hackrf_transfer -r" + str(center_freq/1000000) + ".bin" + " -f" + str(int(center_freq)) + " -s" + str(samp_rate) + " -l" + str(lgain) + " -g" + str(gain) + " -b" + str(int(samp_rate/2)))
        i += 1

def input_data(init_freq, bands, transfer, samp_rate, dtype=np.int8):
    if transfer:
        hackrf_transfer(init_freq, bands, samp_rate)
    binfiles = []
    i = 0
    while i < bands:
        center_freq = init_freq + (i*samp_rate/2)
        binfiles.append(str(center_freq/1000000) + ".bin")
        i += 1
    IQarray = []
    for binfile in binfiles:
        rawdata = np.fromfile(binfile, dtype)
        IQarray.append(rawdata)
    return np.array(IQarray)

def datacheck(data):
    real = data[0::2]
    imag = data[1::2]
    plt.hist(real)
    plt.hist(imag)
    plt.show()

def reducer(data, m):
    rspec = []
    i = 0
    for datum in data:
        if i < m:
            rspec.append(np.median(data[0:i+m]))
            i += 1
        elif i >= (len(data) - m):
            rspec.append(np.median(data[i-m:]))
            i += 1
        else:
            rspec.append(np.median(data[i-m:i+m]))
            i += 1
    return rspec
    
def IQtospec(init_freq, bands, transfer, samp_rate, fftsize, m, xax=0, yax=1):
    IQdata = input_data(init_freq, bands, transfer, samp_rate)
    allavg = []
    for sample in IQdata:
        row = len(sample) / fftsize
        sample = sample.reshape(int(row), fftsize)
        power_array = []
        for row in sample:
            comp = row[0::2] + row[1::2] * 1j
            cfft = np.fft.fft(comp)
            cfft[0] = cfft[1]
            sfft = np.fft.fftshift(cfft)
            power_array.append(abs(sfft)**2)
        indices_arr = np.swapaxes(power_array, xax, yax)
        power_avg = []
        for index in indices_arr:
            power_avg.append(np.average(index))
        allavg = np.append(allavg, power_avg[int(fftsize/8):int(3*fftsize/8)])
    rdata = reducer(allavg, m)
    return rdata
            
def plotspec(init_freq, bands, transfer, samp_rate, fftsize, m):
    startfreq = init_freq - samp_rate/4
    endfreq = init_freq + samp_rate/4 + (bands-1)*samp_rate/2
    y = IQtospec(init_freq, bands, transfer, samp_rate, fftsize, m)
    x = np.linspace(startfreq, endfreq, len(y))
    #plt.xlim(startfreq, endfreq)
    plt.plot(x, np.log(y))
    plt.show()

plotspec(1771000000, 1, False, 20000000, 32768, 20)
    
"""
plotspec(init_freq, bands, transfer, samp_rate, fftsize, m)"""
"""
def GBT(input_size, fftsize):
    a = np.memmap('jack.raw', dtype=np.int8)[0:input_size]
    fftsize = 65536
    row = input_size / fftsize
    sample = a.reshape(int(row), fftsize)
    power_array = []
    for row in sample:
        comp = row[0::2] + row[1::2] * 1j
        cfft = np.fft.fft(comp)
        cfft[0] = cfft[1]
        sfft = np.fft.fftshift(cfft)
        power_array.append(abs(sfft)*2)
    indices_arr = np.swapaxes(power_array, 0, 1)
    power_avg = []
    for index in indices_arr:
        power_avg.append(np.average(index))
    allavg = []
    allavg = np.append(allavg, power_avg)
    plt.plot(np.log(allavg))
    plt.show()

GBT(655360000, 65536)
"""
