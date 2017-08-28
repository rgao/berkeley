import numpy as np
import pylab as plt

moon = np.load('data_moon_140404.npz')
print len(moon['jd'])
def moon_average(y):
    r = 100
    n = 100
    y_avg = np.array([])
    for i in y[r: -r]:
        y_avg = np.append([y_avg],[np.mean(y[n-r: n+r])])
        n = n+1
    return y_avg

x_data = (moon['jd'] - moon['jd'][0]) * 86400
x_moon = x_data[100:40319]

y_data = moon['volts']
y_avg = moon_average(y_data)
y_moon = y_data[100:40319] - y_avg

plt.xlim([0,40320])
plt.title('Moonrise-ish to Moonset-ish')
plt.xlabel('Time(s)')
plt.ylabel('Voltage')

plt.plot(x_moon, y_moon)
plt.show()
