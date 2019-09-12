# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt

f=float(raw_input("frec:"))
N=int(raw_input("Numero de muestras:"))
t=float(raw_input("tiempo de simu:"))
filtro=int(raw_input("Frecuencia de filtro:"))
ab=int(raw_input("AB:"))
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
muestras2=list()

for i in range(0,N):
    if  (filtro-ab <=i and i<=filtro+ab) or (N-ab-filtro<=i and  i<=N-filtro+ab):
        x[i]=0
	y[i]=0
    muestras2.append(float(math.sqrt(math.pow(y[i],2)+math.pow(x[i],2))))

salida=list()
tempo=list()

for i in range(0,N):
    coseno=0
    seno=0
    for j in range(0,N):
        ang=(2*math.pi*i*j)/(N+1)
        aten=float(1/math.sqrt(N+1))
        seno=seno+aten*(y[j]*math.cos(ang)+x[j]*math.sin(ang))
        coseno=coseno+aten*(x[j]*math.cos(ang)-y[j]*math.sin(ang))
    mod=float(math.sqrt(math.pow(coseno,2)+math.pow(seno,2)))
    salida.append(mod)
    tempo.append(coseno)

plt.subplot(411)
plt.plot(tiemp,signal)
plt.subplot(412)
plt.plot(muestr,modulo)
plt.subplot(413)
plt.plot(muestras2)
plt.subplot(414)
plt.plot(tempo)
plt.show()
