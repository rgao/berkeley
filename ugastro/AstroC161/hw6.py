import math
import numpy as np
import pylab   

np.seterr(over=None)

def scale_factor(t):
	a = t**.5
	return a

def n_neutrino(t, n1eV=5e13, k=8.617e-5):
	n = n1eV * (k * time_to_temp(t))**3
	return n

def sigma_neutrino(t, s1MeV=1e-43, k=8.617e-11):
	sigma = s1MeV * (k * time_to_temp(t))**2
    	return sigma

def time_to_temp(t):
	T = 1e10 * t**(-.5)
	return T

def collision_rate(t, n1eV=5e13, s1MeV=1e-43, c=3e10):
	rate = n_neutrino(t) * sigma_neutrino(t) * c
	return rate

def n_over_p_frz(t):
	n_over_p_frz = np.exp((-1.5e10/time_to_temp(t)))
	return n_over_p_frz

def n_over_p_decay(t):
	n_frz = np.exp((-1.5e10/time_to_temp(1)))
	n_over_p_decay = n_frz * np.exp(-t/890.) / (2. - np.exp(-t/890.))
	return n_over_p_decay

def calc_D_over_n(t, eta=5e-10, dE=2.2, k=8.617e-11):
	D_over_n = 6.5 * eta / .001064 * k**1.5 * np.exp(time_to_temp(t), np.ones_like(t) * 1.5) * np.exp(dE / (k*time_to_temp(t)))
	return D_over_n

def p_over_t_0(t, m_p=938.272, k=8.617e-11, h_bar=6.582e-22):
	p_over_t = 2 * (m_p * k * time_to_temp(t) / (2 * 9e20 * np.pi * h_bar**2))**1.5 * np.exp(-m_p / (k * time_to_temp(t)))
	return p_over_t

def n_over_t_0(t, m_n=939.565, k=8.617e-11, h_bar=6.582e-22):
        n_over_t = 2 * (m_n * k * time_to_temp(t) / (2 * 9e20 * np.pi * h_bar**2))**1.5 * np.exp(-m_n / (k * time_to_temp(t))) 
	return n_over_t

def p_over_t_decay(t):
	p_frz = np.exp((-1.5e10/time_to_temp(1)))
        p_over_t_decay = p_frz * (1 + np.exp(-t/890))
        return p_over_t_decay

def n_over_t_decay(t):
	n_frz = np.exp((-1.5e10/time_to_temp(1)))
        n_over_t_decay = n_frz * np.exp(-t/890)
        return n_over_t_decay

def p_over_t(t):
	if t < 1:
		p_over_t_0(t)
	else:
		p_over_t_decay(t)

def n_over_t(t):
        if t < 1:
                n_over_t_0(t)
        else:
		n_over_t_decay(t)




t = np.logspace(-3, 3, num=1000)

pylab.title("BBN: Collision Rate of Weakly Interacting Particles")
pylab.xlabel("Time (s)")
pylab.ylabel("Collision Rate (s-1)")
pylab.xlim(.001, 1000)
pylab.ylim(collision_rate(1000), collision_rate(.001))
pylab.loglog(t, collision_rate(t))
pylab.show()

pylab.title("BBN: Neutron to Proton Ratio")
pylab.xlabel("Time (s)") 
pylab.ylabel("Ratio")
pylab.xlim(.001, 1000)
pylab.ylim(n_over_p_decay(1000), n_over_p_frz(.001))
pylab.loglog(t, np.maximum(n_over_p_frz(t), n_over_p_decay(t)))
pylab.show()

pylab.title("Density of Protons and Neutrons without Decay")
pylab.xlabel("Time (s)")
pylab.ylabel("Baryon Density")
pylab.xlim(.001, 1000)
pylab.ylim(p_over_t_0(1000), p_over_t_0(.001))
pylab.loglog(t, p_over_t_0(t))
pylab.loglog(t, n_over_t_0(t))
pylab.show()

pylab.title("Density of Protons and Neutrons with Decay")
pylab.xlabel("Time (s)")
pylab.ylabel("Baryon Density")
pylab.xlim(.001, 1000)
pylab.ylim(p_over_t_0(1000), p_over_t_0(.001))
pylab.loglog(t, p_over_t(t))
pylab.loglog(t, n_over_t(t))
pylab.show()
