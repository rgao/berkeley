import DFEC
import numpy as np
import matplotlib.gridspec as gds
import matplotlib.pyplot as plt

sample1 = np.load('sample1.npz')
sample2 = np.load('sample2.npz')
sample3 = np.load('sample3.npz')
sample4 = np.load('sample4.npz')
sample5 = np.load('sample5.npz')
sample6 = np.load('sample6.npz')
sample7 = np.load('sample7.npz')
sample8 = np.load('sample8.npz')
sample9 = np.load('sample9.npz')
sample10 = np.load('sample10.npz')
sample11 = np.load('sample11.npz')

x1 = sample1['arr_0']
x2 = sample2['arr_0']
x3 = sample3['arr_0']
x4 = sample4['arr_0']
x5 = sample5['arr_0']
x6 = sample6['arr_0']
x7 = sample7['arr_0']
x8 = sample8['arr_0']
x9 = sample9['arr_0']
x10 = sample10['arr_0']
x11 = sample11['arr_0']
	
y1 = np.fft.fftshift(np.fft.fft(x1))
y2 = np.fft.fftshift(np.fft.fft(x2))
y3 = np.fft.fftshift(np.fft.fft(x3))
y4 = np.fft.fftshift(np.fft.fft(x4))
y5 = np.fft.fftshift(np.fft.fft(x5))
y6 = np.fft.fftshift(np.fft.fft(x6))
y7 = np.fft.fftshift(np.fft.fft(x7))
y8 = np.fft.fftshift(np.fft.fft(x8))
y9 = np.fft.fftshift(np.fft.fft(x9))
y10 = np.fft.fftshift(np.fft.fft(x10))
y11 = np.fft.fftshift(np.fft.fft(x11))

z1 = (abs(y1))**2
z2 = (abs(y2))**2
z3 = (abs(y3))**2
z4 = (abs(y4))**2
z5 = (abs(y5))**2
z6 = (abs(y6))**2
z7 = (abs(y7))**2
z8 = (abs(y8))**2
z9 = (abs(y9))**2
z10 = (abs(y10))**2
z11 = (abs(y11))**2

spec1 = [z1,z3,z7,z9]
spec2 = [z5,z10]
x = np.fft.fftshift(np.fft.fftfreq(256,5e-8))

def specplot1():
	n = 1
	for item in spec1:
		if n < 3:
			m = 4*n - 2
		else:
			m = 4*n + 2
		plt.subplot(2,2,n)
		plt.plot(x,item)
		plt.title(r'$\nu_{sig} =$'+str(m)+'MHz',fontsize=14)
		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Power at 0 dBm')
		plt.xlim(-1.2e7,1.2e7)
		n = n+1

plt.figure(4)
specplot1()
plt.tight_layout()
plt.show()
                                                                                  
def specplot2():
	n = 1
	for item in spec2:
		m = 10*n
		plt.subplot(2,1,n)
		plt.plot(x,item)
		plt.title(r'$\nu_{sig} = $'+str(m)+'MHz',fontsize=14)
		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Power at 0 dBm')
		plt.xlim(-1.2e7,1.2e7)
		n = n+1

plt.figure(5)
specplot2()
plt.tight_layout()
plt.show()

def specplot3():
	plt.plot(x,z11)
       	plt.title(r'$\nu_{sig} = 30 MHz, \nu_{samp} = 100 kHz$',fontsize=14)
       	plt.xlabel('Frequency (Hz)')
       	plt.ylabel('Power at 0 dBm')
       	plt.xlim(-1.2e7,1.2e7)

plt.figure(6)
specplot3()
plt.tight_layout()
plt.show()

