# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt

f=float(input("frec:"))
N=int(input("Numero de muestras:"))
t=float(input("tiempo:"))
tm=float(t/N)
signal=list()
tiemp=list()
tempp=0
for n in range(0,N):
    muestra=float(1*math.sin(2*math.pi*f*n*tm))
    signal.append(muestra)
    tiemp.append(tempp)
    tempp=n*tm
muestr=list()
integral=0
for i in range(0,N):
    integral+=float(signal[i]*tm)
    muestr.append(integral)
plt.subplot(211)
plt.plot(tiemp,signal)
plt.subplot(212)
plt.plot(tiemp,muestr)
plt.show()
