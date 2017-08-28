import numpy as np
import matplotlib.pyplot as plt

a = np.memmap('jack.raw', dtype=np.int8)

def plothist(data):
    plt.hist(data[0::2])
    plt.hist(data[1::2])
    plt.show()

plothist(a[0:65536])
