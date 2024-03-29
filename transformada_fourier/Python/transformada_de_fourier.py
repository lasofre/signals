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
    muestra=float(1*math.sin((2*math.pi*f*n*tm))+1*math.sin((16*math.pi*f*n*tm))+1*math.sin((12*math.pi*f*n*tm)))
    signal.append(muestra)
    tiemp.append(tempp)
    tempp=n*tm

modulo=list()
seno=float(0)
coseno=float(0)
mod=float(0)
muestr=list()
y=list()
x=list()
for i in range(0,N):
    for j in range(0,N):
        ang=(2*math.pi*i*j)/(N+1)
        aten=float(1/math.sqrt(N+1))
        seno=seno-aten*signal[j]*math.sin(ang)
        coseno=coseno+aten*signal[j]*math.cos(ang)
    #print str(coseno)+"+j"+str(seno)
    y.append(seno)
    x.append(coseno)
    mod=float(math.sqrt(math.pow(coseno,2)+math.pow(seno,2)))
    seno=0
    coseno=0
    modulo.append(mod)
    muestr.append(i)
plt.subplot(211)
plt.plot(tiemp,signal)
plt.subplot(212)
plt.plot(muestr,modulo)
plt.show()
