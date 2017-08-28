import numpy as np
import pylab as plt

orion_1 = np.load('data_orion_140321.npz')
orion_2 = np.load('data_orion_140321_2.npz')

def orion_average(y):
    r = 100
    n = 100
    y_avg = np.array([])
    for i in y[r: -r]:
        y_avg = np.append([y_avg],[np.mean(y[n-r: n+r])])
        n = n+1
    return y_avg

x_data = np.append([orion_1['jd'] - orion_1['jd'][0]], [orion_2['jd'] - orion_1['jd'][0]]) * 86400
x_orion = x_data[100:12170]

y_data = np.append([orion_1['volts']],[orion_2['volts']])
y_avg = orion_average(y_data)
y_orion = y_data[100:12170] - y_avg

plt.title('Signals from the Orion Nebula')
plt.xlabel('Time(s)')
plt.ylabel('Voltage')
plt.xlim([0,12250])
plt.plot(x_orion,y_orion)
plt.show()

x_fft = np.fft.fftshift(np.fft.fftfreq(12070,6.67e-8)) / 1000000.
y_fft = np.fft.fftshift(np.fft.fft(y_orion))
y_spec = np.abs(y_fft)**2

plt.title('Power Spectrum of Orion Data')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Power')
plt.plot(x_fft,y_spec)
plt.show()

def orion_filter(y):
    i = 0
    for i in np.arange(len(y)):
        if y[i] < .72:
            y[i] = 0
    i = i+1
    return y

y_filter = orion_filter(y_fft)
y_smooth = np.fft.ifft(np.fft.ifftshift(y_filter))

plt.xlim([0,12250])
plt.plot(x_orion,y_smooth)
plt.show()


