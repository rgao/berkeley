import numpy as np
import pylab as plt

sun = np.load('data_sunrain_140401.npz')

def sun_average(y):
    r = 100
    n = 100
    y_avg = np.array([])
    for i in y[r: -r]:
        y_avg = np.append([y_avg],[np.mean(y[n-r: n+r])])
        n = n+1
    return y_avg

x_data = (sun['jd'] - sun['jd'][0]) * 86400
x_sun = x_data[100:34405]

y_data = sun['volts']
y_avg = sun_average(y_data)
y_sun = y_data[100:34405] - y_avg

Y_F = []
X_F = []
x_0 = []
y_0 = []

i = 0
while i < len(X)-9:
    if YY[i] > .0003:
        y_0.append(YY[i])
        x_0.append(X[i])
        i = i+1
    else:
        while YY[i] < .0003:
            i = i+1
        Y_F.append(np.max(y_0))
        X_F.append(np.mean(x_0))
        y_0 = []
        x_0 = []
    print i





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
