import numpy as np
import matplotlib.pyplot as plt

"""
Work here is done according to instructions of some materials from the Optical/Infrared ugastro lab. Reference: http://ugastro.berkeley.edu/optical/
"""

#time resolution for each interval of photon detection
t_res = 1.0e-6
#total integrated time of sampling
t_int = 1.0
#number of time resolution elements
N_el = t_int / t_res
#expected average number of photons per integratio0n
N_ph = 100.
#probability of at least 1 photon captured in a given t_res
p = 1 - (t_res/t_int)**(N_ph)

def photon_dist(N_ph, N_el):
    """
    distribution of number of photons captured in a given t_res
    """
    result = np.random.randint(N_el, size=N_ph)
    x = np.arange(N_ph + 1)
    int_ph = []
    for i in x:
        photon = 0
        for r in result:
            if i == r:
                photon += 1
        int_ph.append(photon)
    y = []
    for i in x:
        y_ph = 0
        for ph in int_ph:
            if i == ph:
                y_ph += 1
        y.append(y_ph)
    print(x, y)
    plt.title("Number of Photons in each Time-Resolution Interval")
    plt.xlabel("Number of Photons (" + str(N_ph) + " Total)")
    plt.ylabel("Number of t_res Intervals")
    plt.plot(x,y)
    plt.show()

photon_dist(100, 1000000)

