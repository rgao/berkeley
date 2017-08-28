import numpy as np
import matplotlib.pyplot as plt
import DFEC

mix1 = np.load('mixer1.npz')
mixer1 = mix1['arr_0']
x_values = np.arange(len(mixer1))*.5128205128205

plt.figure(8)
plt.subplot(211)
plt.title(r'$\nu_{sig} = \nu_{lo} - \delta\nu, \nu_{s} = 4.1 MHz$',fontsize=14)
plt.xlabel(r'Time $= \mu{s}$')
plt.ylabel('Voltage (V)')
plt.xlim(0,130)
plt.plot(x_values,mixer1)

freq = np.fft.fftshift(np.fft.fftfreq(256,2.564e-7))
mixer1fft = np.fft.fftshift(np.fft.fft(mixer1))                               

plt.subplot(212)
plt.title(r'$\nu_{sig} = \nu_{lo} - \delta\nu, \nu_{s} = 4.1 MHz$',fontsize=14)
plt.xlabel(r'Frequency (Hz)')
plt.ylabel('Voltage (V)')
plt.xlim(-2250000,2250000)
plt.plot(freq,mixer1fft)
plt.tight_layout()
plt.show()

plt.title(r'Spectral Leakable of Plot 2 of Figure 8',fontsize=14)
plt.xlabel(r'Frequency (Hz)')
plt.ylabel('Voltage (V)')
plt.plot(freq,mixer1fft)
plt.show()

