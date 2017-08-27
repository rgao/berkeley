import numpy as np
import pylab as plt
import ephem as ep
import time as t
import sys

obs = ep.Observer()
obs.lat = ep.degrees(37.8732)
obs.long = ep.degrees(-1220.2573)
obs.date = ep.now()
lat = obs.lat * np.pi/180
long = obs.long * np.pi/180

src = ep.FixedBody()
src._ra = sys.argv[1]
src._dec = sys.argv[2]
src._epoch = ep.J2000
src.compute(obs)
ra = float(src.ra)
dec = float(src.dec)

print ra
print dec

x = np.cos(ra) * np.cos(dec)
y = np.sin(ra) * np.cos(dec)
z = np.sin(dec)

R = np.array([[-.054876,-.873437,-.483835],[.494109,.444830,.746982],[-.867666,-.198076,.455984]])
Point = np.array([[x],[y],[z]])

Galactic = np.dot(R, Point)
l = np.mod(np.arctan2(Galactic[1],Galactic[0])*np.pi/180,360)
b = np.arcsin(Galactic[2])

print l, b
