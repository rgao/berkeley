#this first code is for showing the convergence of noise distributions to Gaussian distributions

import numpy as np
import matplotlib.pyplot as plt

x = 10 + np.random.randn(1000)
plt.hist(x,20,normed=1)
plt.title('Random Sample Distribution')
plt.xlabel('Random Sample Values')
plt.ylabel('Frequency as f(value)')
plt.axis([0,10,0,1])
plt.grid(True)
plt.show()

#this next code is for the Allen Variance Test for arbitrary values of samples sizes from 1 to 901

import numpy as np
import matplotlin.pyplot as plt
for n in range (1,901):
    x = np.random.randn(n,1000)
    y[n-1] = np.std(np.mean(x,0))
plt.title('Allen Variance Test')
plt.xlabel('Sample Size N')
plt.ylabel('Standard Deviation of N Random Values')
plt.show()
