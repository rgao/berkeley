import numpy as np
import cPickle as pickle
import pylab as plt

d = pickle.load(open("specs.pkl","rb"))
y = d[66.0,-72.0]

a = y[0][1][0] #online, caloff
b = y[0][1][1] #online, calon
c = y[0][1][2] #offline, caloff
d = y[0][1][3] #offline, calon

T = 100*c/a*np.sum(c)/np.sum(d-c)

plt.plot(T)
plt.show()
