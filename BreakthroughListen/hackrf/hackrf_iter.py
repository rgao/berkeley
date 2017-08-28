
import os

def hackrf_scan(n, filename, center_freq, timeout=5, lgain=24, gain=30, samp_rate=16000000):
    i = 0 
    while i < n:
        os.system("timeout " + str(timeout) +"s hackrf_transfer -r" + filename + " -f" + str(center_freq + (i * samp_rate)) + " -s" + str(samp_rate) + " -l" + str(lgain) + " -g" + str(gain) + " -b" + str(8000000))
        i += 1  

hackrf_scan(1, "2445.bin", 2445000000)



