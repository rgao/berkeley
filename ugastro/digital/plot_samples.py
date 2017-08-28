import DFEC
import numpy as np
import matplotlib.pyplot as plt

x1 = np.load('sample1.npz')
x2 = np.load('sample2.npz')
x3 = np.load('sample3.npz')
x4 = np.load('sample4.npz')
x5 = np.load('sample5.npz')
x6 = np.load('sample6.npz')
x7 = np.load('sample7.npz')
x8 = np.load('sample8.npz')
x9 = np.load('sample9.npz')

time = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
x = np.arange(0, 1e-6, 1e-6/256)

y1 = np.fft.fft(x1)
y2 = np.fft.fft(x2)
y3 = np.fft.fft(x3)
y4 = np.fft.fft(x4)
y5 = np.fft.fft(x5)
y6 = np.fft.fft(x6)
y7 = np.fft.fft(x7)
y8 = np.fft.fft(x8)
y9 = np.fft.fft(x9)

freq = [y1,y2,y3,y4,y5,y6,y7,y8,y9]

def plottime():
	n = 1
	for item in time:
		plt.subplot(3,3,n)
		plt.plot(x, item)
		n = n+1

plt.figure(1)
plottime()
plt.show()
