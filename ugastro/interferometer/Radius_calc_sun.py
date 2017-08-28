import numpy as np
import matplotlib.pyplot as plt

#############################
# Leonardo Sattler Cassara
# Code to analyse the Sun
#############################

f = 'data_sunrain_140401.npz'

data = np.load(f)

x = data['jd']

y = data['volts']


## Smoothing Function ##

SM=[] 
r = 100
while r < len(x)-100:
    box = np.arange(r-100,r+101)
    SM.append(np.median(y[box]))
    r = r+1

X = x[100:-100]
Y = y[100:-100]-SM


YY = []

for i in Y:
    if i < 0:
        i = 0.
        YY.append(i)
    else:
        YY.append(i)
        

## Finding the Shape ##

Y_F = []
X_F = []
x_0 = []
y_0 = []

i = 0
while i < len(X)-9:
    if YY[i] > .0003:
        y_0.append(YY[i])
        x_0.append(X[i])
        i = i+1
    else:
        while YY[i] < .0003:
            i = i+1
        Y_F.append(np.max(y_0))
        X_F.append(np.mean(x_0))
        y_0 = []
        x_0 = []
    print i


## Least Square 2 (from casper) ##

Y_2 = Y_F[167:210]
X_FF = X_F[167:210]


h_a = (data['lst'][167:210] - data['ra'][167:210])*np.pi/12.
B = 10.
lamb = 2.8*10**(-2)
dec = data['dec'][167:210]*np.pi/180.

chi = [] 

phi = np.arange(0,2*np.pi,0.01) ## Evaluating phi
for i in phi:
    F_t = np.cos(2*np.pi * ( (B/lamb) * np.cos(dec) * np.sin(h_a)) + i)

    X_2 = np.empty([len(F_t),3])
    X_2[:,0] = 1*F_t
    X_2[:,1]= h_a*F_t
    X_2[:,2]= (h_a**2) * F_t

    X_X = np.dot(np.transpose(X_2),X_2)

    XY = np.dot(np.transpose(X_2),Y_2)

    XXI = np.linalg.inv(X_X)

    a = np.dot(XY,XXI)

    YBAR = np.dot(X_2,a)

    res = Y_2 - YBAR 
    
    chi.append(np.sum(res**2))

phi_min=phi[list(chi).index(np.min(chi))] ## Finding minimum phi

F_t = np.cos(2*np.pi * ( (B/lamb) * np.cos(dec) * np.sin(h_a)) + phi_min)

X_2 = np.empty([len(F_t),3])
X_2[:,0] = 1*F_t
X_2[:,1]= h_a*F_t
X_2[:,2]= (h_a**2) * F_t

X_X = np.dot(np.transpose(X_2),X_2)

XY = np.dot(np.transpose(X_2),Y_2)

XXI = np.linalg.inv(X_X)

a = np.dot(XY,XXI)

YBAR = np.dot(X_2,a)


plt.subplot(2,1,1)
plt.title('Sun Window',size=26)
plt.plot(X,YY,'b-') 
plt.plot(X_F[167:210],Y_F[167:210],'r-')
plt.rc('ytick', labelsize=12)
plt.rc('xtick', labelsize=12) 
plt.ylabel('Power Spectra' + r' $[V]^{2}$',size=23)
plt.xlabel('Julian Date [Decimal Days]',size=23)

plt.subplot(2,1,2)
plt.title('Sun Window - Zoom',size=26)
plt.plot(X,YY,'b-') 
plt.plot(X_F[167:210],Y_F[167:210],'r-')
plt.rc('ytick', labelsize=12)
plt.rc('xtick', labelsize=12) 
plt.ylabel('Power Spectra' + r' $[V]^{2}$',size=23)
plt.xlabel('Julian Date [Decimal Days]',size=23)

plt.subplots_adjust(hspace=0.5)
plt.show()

X_2[:,0] = 1
X_2[:,1]= h_a
X_2[:,2]= (h_a**2)
YBAR_plot = np.dot(X_2,a) * np.pi/12

plt.title('Parabolic Least-Squares Fit for Moon Sun Data',size=18)
plt.plot(h_a, YBAR_plot) 
plt.rc('ytick', labelsize=12)
plt.rc('xtick', labelsize=12) 
plt.ylabel(r'Power (V$^2$)', size=15)
plt.xlabel('Hour Angle (radians)', size=15)
plt.plot(h_a, YBAR_plot)
plt.show()

N = 1000

f_f = B*np.cos(dec[list(YBAR).index(np.min(YBAR))  ## fringe frequency
])*np.cos(h_a[list(YBAR).index(np.min(YBAR))
])/lamb

## Solving Integral Numerically ##

M_f = []
q1 = []
q2 = []

k=0
M_f = []
I = np.arange(0,6,0.01)
for i in I:
    for n in np.arange(-N,N+1):
        q1.append(np.sqrt(1 - (n/N)**2))
        q2.append(np.cos(2.*np.pi*i*n/N))
    M_f.append(np.sum(q1)*np.sum(q2))
    q1 = []
    q2 = []
    
    k=k+1

plt.title(r'$MF_{theory}$ vs' + r' $f_{f}R_{Sun}$',size=18)
plt.plot(I,M_f)
plt.rc('ytick', labelsize=12)
plt.rc('xtick', labelsize=12) 
plt.ylabel(r'$MF_{theory}$',size=15)
plt.xlabel(r'$R \cdot f_{f}$',size=15)
plt.axhline(y = 0, color = 'r')
plt.show()


z = []
I_2 = []
M_f.append(1.)

i = 0
while i < len(M_f):
    if M_f[i] > 0.:
        i=i+1
    else:
        z.append(i)
        I_2.append(I[i])
        while M_f[i] < 0.:
            i = i+1
    

rr = I_2[0]/f_f
rr*180./np.pi

print 
print 'Radius = ', rr, ' in radians'
print
print 'F_f = ', f_f
