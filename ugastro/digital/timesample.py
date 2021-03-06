import numpy as np
import matplotlib.pyplot as plt
import DFEC

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

time1 = [x1,x3,x7,x9]
time2 = [x5,x10]
x_axis = np.arange(256) * .05

def timeplot1():
	n = 1
	for item in time1:
		if n < 3:
			m = 4*n - 2
		else:
			m = 4*n + 2
		plt.subplot(2,2,n)
		plt.plot(x_axis,item)
		plt.title(r'$\nu_{sig} =$'+str(m)+'MHz',fontsize=14)
		plt.xlabel(r'Time ($\mu{s}$)')
		plt.ylabel('Voltage (V)')
		plt.xlim(0,12.8)
		n = n+1

plt.figure(1)
timeplot1()
plt.tight_layout()
plt.show()
                                                                                  
def timeplot2():
	n = 1
	for item in time2:
		m = 10*n
		plt.subplot(2,1,n)
		plt.plot(x_axis,item)
		plt.title(r'$\nu_{sig} =$'+str(m)+'MHz',fontsize=14)
		plt.xlabel(r'Time ($\mu{s}$)')
		plt.ylabel('Voltage (V)')
		plt.xlim(0,12.8)
		n = n+1
	
plt.figure(2)
timeplot2()
plt.tight_layout()
plt.show()

def timeplot3():
	plt.plot(x_axis,x11)
	plt.title(r'$\nu_{sig} = 30 MHz, \nu_{samp} = 100 kHz$',fontsize=14)
	plt.xlabel(r'Time ($\mu{s}$)')
	plt.ylabel('Voltage (V)')

plt.figure(3)
timeplot3()
plt.tight_layout()
plt.show()
	
