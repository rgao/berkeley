import numpy as np
import pylab as plt

orion_1 = np.load('data_orion_140321.npz')
orion_2 = np.load('data_orion_140321_2.npz')

orion_x = np.append(orion_1['lst'],orion_2['lst']) 
orion = orion_x * np.pi/12      
Y = np.append(orion_1['volts'],orion_2['volts'])

h_s = orion - 1.463
C = 223.407 * np.array(np.arange(9.5,10.5,.001))

r = []

for i in C:
    z = i * np.sin(h_s)
    X = np.array([np.cos(z),-np.sin(z)])
    X_T = np.transpose(X)
    XX = np.dot(X,X_T)
    XY = np.dot(Y,X_T)
    XXI = np.linalg.inv(XX)
    a = np.dot(XY,XXI)
    YBAR = np.dot(a,X)
    DELY = Y-YBAR
    r.append(np.sum(np.abs(DELY)**2))

R = np.array(r) 

plt.plot(C,R)
plt.title('Residual vs. Corresponding C Values of Baseline Lengths')
plt.xlabel('C')
plt.ylabel('Residual')
plt.show()



