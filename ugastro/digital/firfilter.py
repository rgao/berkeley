import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1000000,1000000)

print x

def y():
    for i in x:
        if abs(i) > 62500000:
            return 0
        else:
            return 1

print y

plt.plot(x,y)
plt.show()
